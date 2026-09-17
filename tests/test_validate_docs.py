from pathlib import Path
import json
import re
import shutil
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_docs import validate


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
        self.assertTrue(any("60 unique" in error for error in validate(self.fixture)))

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
        self.assertTrue(any("ten fictional startups" in error for error in errors))
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


if __name__ == "__main__":
    unittest.main()
