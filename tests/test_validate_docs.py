from pathlib import Path
from datetime import date, timedelta
import json
import re
import shutil
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_docs import synchronize_navigation, validate, without_generated_metadata


class DocumentationValidationTests(unittest.TestCase):
    def setUp(self):
        local = ROOT / ".local"
        local.mkdir(exist_ok=True)
        temporary = tempfile.TemporaryDirectory(prefix="guide-test-", dir=local)
        self.addCleanup(temporary.cleanup)
        self.fixture = Path(temporary.name) / "repo"
        shutil.copytree(ROOT, self.fixture, ignore=shutil.ignore_patterns(".local", ".git", "__pycache__", ".venv"))

    def change_json(self, relative, operation):
        path = self.fixture / relative
        data = json.loads(path.read_text(encoding="utf-8"))
        operation(data)
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def test_complete_repository_passes(self):
        self.assertEqual(validate(self.fixture), [])

    def test_broken_link_fails(self):
        path = self.fixture / "README.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[Broken](missing.md)\n", encoding="utf-8")
        self.assertTrue(any("broken or escaping local link" in error for error in validate(self.fixture)))

    def test_missing_question_fails(self):
        self.change_json("tests/scenarios.json", lambda data: data["scenarios"].pop())
        self.assertTrue(any("registered scenario IDs" in error for error in validate(self.fixture)))

    def test_original_baseline_question_cannot_be_removed(self):
        self.change_json("tests/scenarios.json", lambda data: data["scenarios"].pop(0))
        self.assertTrue(any("original 60 baseline" in error for error in validate(self.fixture)))

    def test_unknown_guide_fails(self):
        self.change_json("tests/scenarios.json", lambda data: data["scenarios"][0]["guides"].append("unknown-guide"))
        self.assertTrue(any("unknown guide" in error for error in validate(self.fixture)))

    def test_empty_workflow_section_fails(self):
        path = self.fixture / "guides/shared/context-and-tools.md"
        text = re.sub(r"(## Read-only checks\n).*?(?=\n## )", r"\1", path.read_text(encoding="utf-8"), flags=re.DOTALL)
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("empty or missing section" in error for error in validate(self.fixture)))

    def test_unapproved_source_fails(self):
        path = self.fixture / "guides/accounts/credits.md"
        text = path.read_text(encoding="utf-8").replace("https://learn.microsoft.com/", "https://unapproved.invalid/")
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("unapproved reference" in error for error in validate(self.fixture)))

    def test_one_way_coverage_claim_fails(self):
        path = self.fixture / "guides/accounts/credits.md"
        path.write_text(path.read_text(encoding="utf-8").replace("S01-Q1, ", ""), encoding="utf-8")
        self.assertTrue(any("coverage differ" in error for error in validate(self.fixture)))

    def test_escaping_catalog_path_fails(self):
        self.change_json("catalog.json", lambda data: data["modules"][0].update(path="../outside.md"))
        self.assertTrue(any("invalid repository-relative path" in error for error in validate(self.fixture)))

    def test_reference_example_cannot_claim_live_findings(self):
        self.change_json("examples/result.example.json", lambda data: data.update(status="verified"))
        self.assertTrue(any("must not claim customer observations" in error for error in validate(self.fixture)))

    def test_duplicate_workflow_heading_fails(self):
        path = self.fixture / "guides/shared/context-and-tools.md"
        text = path.read_text(encoding="utf-8").replace("## Read-only checks", "## Read-only checks\nDuplicate.\n\n## Read-only checks")
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("required headings" in error for error in validate(self.fixture)))

    def test_invalid_json_field_types_are_reported(self):
        self.change_json("tests/scenarios.json", lambda data: data["startups"][0].update(id=[]))
        self.change_json("tests/scenarios.json", lambda data: data["scenarios"][0].update(baseline_status=[]))
        errors = validate(self.fixture)
        self.assertTrue(any("baseline startup profiles" in error for error in errors))
        self.assertTrue(any("invalid baseline status" in error for error in errors))

    def test_each_guide_requires_corresponding_azure_website(self):
        path = self.fixture / "guides/accounts/credits.md"
        text = re.sub(r"### Azure website\n.*?(?=### Technical documentation)", "", path.read_text(encoding="utf-8"), flags=re.DOTALL)
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("missing corresponding Azure website" in error for error in validate(self.fixture)))

    def test_azure_website_does_not_replace_technical_documentation(self):
        path = self.fixture / "guides/accounts/credits.md"
        text = re.sub(r"### Technical documentation\n.*?(?=## Scenario coverage)", "", path.read_text(encoding="utf-8"), flags=re.DOTALL)
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("missing corresponding Technical documentation" in error for error in validate(self.fixture)))

    def test_extension_group_with_one_question_and_one_role_passes(self):
        registry = json.loads((self.fixture / "tests/scenarios.json").read_text(encoding="utf-8"))
        group_id = f"S{max(int(group['id'][1:]) for group in registry['startups']) + 1:02d}"
        question_id = f"{group_id}-Q1"

        def add_extension(data):
            data["startups"].append({"id": group_id, "description": "Synthetic extension fixture", "question_ids": [question_id]})
            data["scenarios"].append({
                "id": question_id, "startup": group_id, "role": "Reviewer",
                "question": "Where is the existing support request status?",
                "baseline_status": None, "guides": ["support"],
            })
        self.change_json("tests/scenarios.json", add_extension)
        path = self.fixture / "guides/support/escalation.md"
        path.write_text(path.read_text(encoding="utf-8").rstrip() + f", {question_id}\n", encoding="utf-8")
        self.assertEqual(validate(self.fixture), [])

    def test_extension_must_register_expected_question_ids(self):
        self.change_json("tests/scenarios.json", lambda data: data["startups"][-1].pop("question_ids"))
        self.assertTrue(any("declare expected question_ids" in error for error in validate(self.fixture)))

    def test_unregistered_question_cannot_be_added(self):
        def add_question(data):
            data["scenarios"].append({
                "id": "S13-Q6", "startup": "S13", "role": "Reviewer",
                "question": "An unregistered question.", "baseline_status": None, "guides": ["support"],
            })
        self.change_json("tests/scenarios.json", add_question)
        self.assertTrue(any("registered scenario IDs" in error for error in validate(self.fixture)))

    def test_duplicate_registered_question_fails(self):
        self.change_json("tests/scenarios.json", lambda data: data["startups"][-1]["question_ids"].append("S13-Q1"))
        self.assertTrue(any("duplicate or mismatched registered question" in error for error in validate(self.fixture)))

    def test_new_question_does_not_rewrite_baseline_statistics(self):
        self.change_json("tests/scenarios.json", lambda data: data["scenarios"][-1].update(baseline_status="explicit"))
        errors = validate(self.fixture)
        self.assertTrue(any("extension question must use baseline_status null" in error for error in errors))
        self.assertFalse(any("baseline counts changed" in error for error in errors))

    def test_original_baseline_statistics_still_protected(self):
        self.change_json("tests/scenarios.json", lambda data: data["scenarios"][0].update(baseline_status="missing"))
        self.assertTrue(any("baseline counts changed" in error for error in validate(self.fixture)))

    def test_unknown_guide_status_is_rejected(self):
        self.change_json("catalog.json", lambda data: data["modules"][0].update(status="approved"))
        self.assertTrue(any("missing or invalid guide status" in error for error in validate(self.fixture)))

    def test_missing_guide_status_is_not_silently_assumed(self):
        self.change_json("catalog.json", lambda data: data["modules"][0].pop("status"))
        self.assertTrue(any("missing or invalid guide status" in error for error in validate(self.fixture)))

    def test_catalog_and_header_status_must_match(self):
        self.change_json("catalog.json", lambda data: data["modules"][0].update(status="draft"))
        self.assertTrue(any("catalog and guide status differ" in error for error in validate(self.fixture)))

    def test_draft_cannot_claim_a_review_date(self):
        path = self.fixture / "guides/accounts/costs.md"
        path.write_text(path.read_text(encoding="utf-8").replace("[set on review]", date.today().isoformat()), encoding="utf-8")
        self.assertTrue(any("draft must keep the pending review date" in error for error in validate(self.fixture)))

    def test_draft_must_explicitly_prohibit_execution(self):
        path = self.fixture / "guides/accounts/costs.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Do not execute", "Execute"), encoding="utf-8")
        self.assertTrue(any("draft scope" in error for error in validate(self.fixture)))

    def test_reviewed_guide_requires_real_date(self):
        path = self.fixture / "guides/accounts/credits.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Policy checked: 2026-09-17.", "Policy checked: [set on review]."), encoding="utf-8")
        self.assertTrue(any("real nonfuture ISO" in error for error in validate(self.fixture)))

    def test_reviewed_guide_date_is_independent_of_catalog_baseline(self):
        path = self.fixture / "guides/accounts/credits.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Policy checked: 2026-09-17.", "Policy checked: 2026-09-16."), encoding="utf-8")
        self.assertEqual(validate(self.fixture), [])

    def test_future_review_date_is_rejected(self):
        path = self.fixture / "guides/accounts/credits.md"
        future = (date.today() + timedelta(days=1)).isoformat()
        path.write_text(path.read_text(encoding="utf-8").replace("Policy checked: 2026-09-17.", f"Policy checked: {future}."), encoding="utf-8")
        self.assertTrue(any("real nonfuture ISO" in error for error in validate(self.fixture)))

    def test_reviewed_guide_cannot_hide_unresolved_review_comments(self):
        path = self.fixture / "guides/accounts/credits.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n<!-- REVIEW: Synthetic unresolved issue. -->\n", encoding="utf-8")
        self.assertTrue(any("unresolved REVIEW comments require draft" in error for error in validate(self.fixture)))

    def make_tenant_tested_fixture(self):
        self.change_json("catalog.json", lambda data: data["modules"][0].update(status="tenant-tested"))
        path = self.fixture / "guides/shared/context-and-tools.md"
        text = path.read_text(encoding="utf-8").replace("Status: source-reviewed; not tenant-tested.", "Status: tenant-tested; scoped evidence recorded.")
        path.write_text(text, encoding="utf-8")

    def test_tenant_tested_needs_evidence_metadata(self):
        self.make_tenant_tested_fixture()
        self.assertTrue(any("needs scoped evidence metadata" in error for error in validate(self.fixture)))

    def test_tenant_tested_accepts_complete_synthetic_evidence_shape(self):
        self.make_tenant_tested_fixture()
        path = self.fixture / "reference/tenant-tests/schema-fixture.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Synthetic schema test only. No real tenant was tested.\n", encoding="utf-8")
        self.change_json("catalog.json", lambda data: data["modules"][0].update(tenant_test={
            "tested_on": date.today().isoformat(), "scope": "synthetic-format-fixture",
            "evidence": "reference/tenant-tests/schema-fixture.md",
        }))
        self.assertEqual(validate(self.fixture), [])

    def test_tenant_evidence_cannot_point_to_private_runtime_data(self):
        self.make_tenant_tested_fixture()
        self.change_json("catalog.json", lambda data: data["modules"][0].update(tenant_test={
            "tested_on": date.today().isoformat(), "scope": "synthetic-format-fixture",
            "evidence": ".local/private.json",
        }))
        self.assertTrue(any("sanitized record under reference/tenant-tests" in error for error in validate(self.fixture)))

    def test_only_exact_additional_official_hosts_are_allowed(self):
        path = self.fixture / "guides/accounts/compliance-terms.md"
        text = path.read_text(encoding="utf-8").replace("https://www.microsoft.com/", "https://www.microsoft.com.example.invalid/")
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("unapproved reference URL" in error for error in validate(self.fixture)))

    def test_quota_guide_retains_concrete_tier_lookup(self):
        text = (self.fixture / "guides/models/quotas-tiers-and-capacity.md").read_text(encoding="utf-8")
        for expected in ("az rest --method get", "providers/Microsoft.CognitiveServices/quotaTiers", "currentTierName", "assignmentDate", "tierUpgradePolicy"):
            with self.subTest(expected=expected):
                self.assertIn(expected, text)

    def test_routing_requires_explicit_service_scope(self):
        self.change_json("catalog.json", lambda data: data["modules"][0].pop("service_scope"))
        self.assertTrue(any("routing service_scope" in error for error in validate(self.fixture)))

    def test_navigation_rejects_unknown_targets(self):
        self.change_json("catalog.json", lambda data: data["modules"][0]["navigation"]["related"].append("missing-task"))
        self.assertTrue(any("unknown navigation target" in error for error in validate(self.fixture)))

    def test_stale_task_card_is_reported(self):
        self.change_json("catalog.json", lambda data: data["modules"][0].update(expected_output="A changed outcome."))
        self.assertTrue(any("stale generated task card" in error for error in validate(self.fixture)))

    def test_sync_refreshes_metadata_without_rewriting_policy(self):
        path = self.fixture / "guides/shared/context-and-tools.md"
        original = without_generated_metadata(path.read_text(encoding="utf-8"))
        self.change_json("catalog.json", lambda data: data["modules"][0].update(expected_output="A changed outcome."))
        self.assertEqual(synchronize_navigation(self.fixture), [])
        self.assertEqual(without_generated_metadata(path.read_text(encoding="utf-8")), original)
        synchronized = path.read_bytes()
        self.assertEqual(synchronize_navigation(self.fixture), [])
        self.assertEqual(path.read_bytes(), synchronized)
        self.assertEqual(validate(self.fixture), [])

    def test_invalid_sync_target_prevents_all_writes(self):
        path = self.fixture / "guides/shared/context-and-tools.md"
        original = path.read_bytes()
        self.change_json("catalog.json", lambda data: data["modules"][-1].update(path="../outside.md"))
        self.assertTrue(any("invalid repository-relative path" in error for error in synchronize_navigation(self.fixture)))
        self.assertEqual(path.read_bytes(), original)

    def test_both_readme_indexes_must_link_every_guide(self):
        for name in ("README.md", "README.zh-CN.md"):
            path = self.fixture / name
            text = re.sub(r"\[([^\]]*)\]\(guides/support/escalation\.md\)", r"\1", path.read_text(encoding="utf-8"))
            path.write_text(text, encoding="utf-8")
        errors = validate(self.fixture)
        self.assertTrue(any("README.md: missing guide entry: guides/support/escalation.md" in error for error in errors))
        self.assertTrue(any("README.zh-CN.md: missing guide entry: guides/support/escalation.md" in error for error in errors))

    def test_reader_cards_records_and_source_packet_links_are_checked(self):
        resources = ("start/founder.md", "start/founder.zh-CN.md", "reference/cloud-ops-records.md", "reference/source-review.md")
        for relative in resources:
            path = self.fixture / relative
            path.write_text(path.read_text(encoding="utf-8") + "\n[Broken](missing-reader-page.md)\n", encoding="utf-8")
        errors = validate(self.fixture)
        for relative in resources:
            with self.subTest(relative=relative):
                self.assertTrue(any(str(Path(relative)) in error and "broken or escaping local link" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
