"""Validate documentation structure and fictional coverage without contacting Azure."""

from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit


HEADINGS = (
    "Scope and prerequisites",
    "Official policy and live state",
    "Read-only checks",
    "Interpretation and decisions",
    "Changes and approval",
    "Verification and escalation",
    "Sources",
    "Scenario coverage",
)
AZURE_WEBSITE_HOSTS = {"azure.microsoft.com", "azure.com"}
REFERENCE_HOSTS = {
    "learn.microsoft.com", "docs.github.com", "code.claude.com",
    "www.microsoft.com", "servicetrust.microsoft.com",
} | AZURE_WEBSITE_HOSTS
GUIDE_STATUSES = {"draft", "source-reviewed", "tenant-tested"}
BASELINE_STARTUPS = {f"S{number:02d}" for number in range(1, 11)}
BASELINE_CASES = {f"S{startup:02d}-Q{question}" for startup in range(1, 11) for question in range(1, 7)}
BASELINE_COUNTS = Counter({"explicit": 44, "partial": 12, "missing": 4})
CASE_ID = r"S\d{2,}-Q[1-9]\d*"
CORE_DOCS = (
    "README.md",
    "README.zh-CN.md",
    "AGENTS.md",
    "CLAUDE.md",
    ".github/copilot-instructions.md",
    "reference/result-contract.md",
)


def read_object(path: Path, errors: list[str]) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        errors.append(f"{path.name}: cannot read JSON: {error}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{path.name}: expected a JSON object")
        return None
    return data


def repository_path(root: Path, relative: str) -> Path:
    relative_path = PurePosixPath(relative)
    if not relative or "\\" in relative or relative_path.is_absolute() or ".." in relative_path.parts:
        raise ValueError(f"invalid repository-relative path: {relative!r}")
    result = root.joinpath(*relative_path.parts).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError(f"path escapes repository: {relative!r}")
    return result


def sections(text: str) -> dict[str, str]:
    parts = re.split(r"^## (.+)\s*$", text, flags=re.MULTILINE)
    return {parts[index].strip(): parts[index + 1].strip() for index in range(1, len(parts), 2)}


def valid_review_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        return False
    return parsed.isoformat() == value and parsed <= date.today()


def check_maturity(root: Path, module: dict, text: str, boundary: str, errors: list[str]) -> None:
    identifier, status = module["id"], module.get("status")
    if not isinstance(status, str) or status not in GUIDE_STATUSES:
        errors.append(f"{identifier}: missing or invalid guide status")
        return
    headers = re.findall(r"^Policy checked: (.+?)\. Status: ([a-z-]+); ([^\n]+)$", text, flags=re.MULTILINE)
    if len(headers) != 1:
        errors.append(f"{identifier}: expected one policy/status header")
        return
    checked, header_status, detail = headers[0]
    if header_status != status:
        errors.append(f"{identifier}: catalog and guide status differ")
    if status == "draft":
        if checked != "[set on review]" or "sources not re-verified" not in detail or "not tenant-tested" not in detail:
            errors.append(f"{identifier}: draft must keep the pending review date and unverified disclaimers")
        if "reference only" not in boundary or "do not execute" not in boundary:
            errors.append(f"{identifier}: draft scope must be reference only and prohibit execution")
        return
    if not valid_review_date(checked):
        errors.append(f"{identifier}: reviewed guide needs a real nonfuture ISO policy-check date")
    if "not re-verified" in detail:
        errors.append(f"{identifier}: reviewed status contradicts the unverified disclaimer")
    if re.search(r"<!--\s*REVIEW:", text):
        errors.append(f"{identifier}: unresolved REVIEW comments require draft status")
    if status == "source-reviewed":
        if "not tenant-tested" not in detail:
            errors.append(f"{identifier}: source-reviewed guide must disclaim tenant testing")
        return
    if "not tenant-tested" in detail:
        errors.append(f"{identifier}: tenant-tested status contradicts its header")
    record = module.get("tenant_test")
    if not isinstance(record, dict):
        errors.append(f"{identifier}: tenant-tested guide needs scoped evidence metadata")
        return
    if not valid_review_date(record.get("tested_on")) or not isinstance(record.get("scope"), str) or not record["scope"].strip():
        errors.append(f"{identifier}: tenant evidence needs a date and nonempty scope label")
    evidence = record.get("evidence")
    if not isinstance(evidence, str):
        errors.append(f"{identifier}: tenant evidence needs a repository-relative record")
        return
    try:
        path = repository_path(root, evidence)
    except ValueError as error:
        errors.append(f"{identifier}: {error}")
        return
    if not path.is_relative_to(root / "reference" / "tenant-tests") or path.suffix not in {".md", ".json"}:
        errors.append(f"{identifier}: tenant evidence must be a sanitized record under reference/tenant-tests")
        return
    try:
        if not path.read_text(encoding="utf-8").strip():
            errors.append(f"{identifier}: tenant evidence record is empty")
    except (OSError, UnicodeError) as error:
        errors.append(f"{identifier}: tenant evidence cannot be read: {error}")


def registered_questions(startups: list, errors: list[str]) -> tuple[set[str], set[str]]:
    group_ids: set[str] = set()
    expected = set(BASELINE_CASES)
    for group in startups:
        if not isinstance(group, dict):
            errors.append("invalid scenario group object")
            continue
        identifier = group.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(r"S\d{2,}", identifier) or identifier in group_ids:
            errors.append("invalid or duplicate scenario group id")
            continue
        group_ids.add(identifier)
        if not isinstance(group.get("description"), str) or not group["description"].strip():
            errors.append(f"{identifier}: scenario group needs a description")
        declared = group.get("question_ids")
        if declared is None and identifier in BASELINE_STARTUPS:
            continue
        if not isinstance(declared, list) or not declared or not all(isinstance(item, str) for item in declared):
            errors.append(f"{identifier}: extension group must declare expected question_ids")
            continue
        if len(declared) != len(set(declared)) or any(
            not re.fullmatch(CASE_ID, item) or not item.startswith(identifier + "-") for item in declared
        ):
            errors.append(f"{identifier}: invalid, duplicate or mismatched registered question ID")
            continue
        original = {item for item in BASELINE_CASES if item.startswith(identifier + "-")}
        if not original.issubset(declared):
            errors.append(f"{identifier}: registration cannot remove original baseline questions")
        expected.update(declared)
    if not BASELINE_STARTUPS.issubset(group_ids):
        errors.append("registry must retain all original baseline startup profiles")
    return group_ids, expected


def check_links(root: Path, path: Path, text: str, errors: list[str]) -> None:
    for target in re.findall(r"!?\[[^\]]*\]\(([^)\s]+)\)", text):
        try:
            parsed = urlsplit(target)
        except ValueError as error:
            errors.append(f"{path.relative_to(root)}: invalid link {target!r}: {error}")
            continue
        if parsed.scheme:
            continue
        destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if not destination.is_relative_to(root.resolve()) or not destination.is_file():
            errors.append(f"{path.relative_to(root)}: broken or escaping local link: {target}")
            continue
        if parsed.fragment and destination.suffix == ".md":
            headings = re.findall(r"^#+ (.+)$", destination.read_text(encoding="utf-8"), flags=re.MULTILINE)
            anchors = {re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-") for heading in headings}
            if unquote(parsed.fragment) not in anchors:
                errors.append(f"{path.relative_to(root)}: unknown local anchor: {target}")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    catalog = read_object(root / "catalog.json", errors)
    registry = read_object(root / "tests" / "scenarios.json", errors)
    if catalog is None or registry is None:
        return errors
    modules = catalog.get("modules")
    cases = registry.get("scenarios")
    startups = registry.get("startups")
    if not isinstance(modules, list) or not modules or not isinstance(cases, list) or not cases or not isinstance(startups, list) or not startups:
        return errors + ["catalog/modules and registry/startups/scenarios must be nonempty lists"]
    if not valid_review_date(catalog.get("reviewed_on")):
        return errors + ["catalog reviewed_on must be a nonfuture ISO baseline date"]

    module_paths: dict[str, Path] = {}
    declared_cases: dict[str, set[str]] = {}
    documents: dict[Path, str] = {}
    for module in modules:
        if not isinstance(module, dict) or not isinstance(module.get("id"), str) or not isinstance(module.get("path"), str):
            errors.append("invalid module object")
            continue
        identifier = module["id"]
        if not re.fullmatch(r"[a-z][a-z0-9-]*", identifier) or identifier in module_paths:
            errors.append(f"invalid or duplicate module id: {identifier}")
            continue
        try:
            path = repository_path(root, module["path"])
        except ValueError as error:
            errors.append(str(error))
            continue
        if path in module_paths.values() or not path.is_relative_to(root / "guides") or path.suffix != ".md":
            errors.append(f"{identifier}: expected a unique guide Markdown path")
            continue
        module_paths[identifier] = path
        if not path.is_file():
            errors.append(f"{identifier}: guide missing: {module['path']}")
            continue
        text = path.read_text(encoding="utf-8")
        documents[path] = text
        contents = sections(text)
        found_headings = tuple(heading.strip() for heading in re.findall(r"^## (.+)$", text, flags=re.MULTILINE))
        if found_headings != HEADINGS:
            errors.append(f"{identifier}: required headings missing, duplicated or out of order")
        for heading in HEADINGS:
            if not contents.get(heading):
                errors.append(f"{identifier}: empty or missing section: {heading}")
        boundary = contents.get("Scope and prerequisites", "").lower()
        check_maturity(root, module, text, boundary, errors)
        if "read-only" not in boundary or "approval" not in boundary:
            errors.append(f"{identifier}: standalone scope must state read-only mode and approval")
        source_text = contents.get("Sources", "")
        urls = re.findall(r"https://[^\s<>]+", source_text)
        if not urls:
            errors.append(f"{identifier}: missing official sources")
        for url in urls:
            try:
                parsed = urlsplit(url)
            except ValueError as error:
                errors.append(f"{identifier}: invalid reference URL: {error}")
                continue
            if parsed.hostname not in REFERENCE_HOSTS or parsed.username or parsed.password:
                errors.append(f"{identifier}: unapproved reference URL: {url}")
        for category, hosts in (
            ("Azure website", AZURE_WEBSITE_HOSTS),
            ("Technical documentation", {"learn.microsoft.com"}),
        ):
            block = re.search(r"^### " + re.escape(category) + r"\n(.*?)(?=^### |\Z)", source_text, flags=re.MULTILINE | re.DOTALL)
            matching = False
            if block:
                for url in re.findall(r"https://[^\s<>]+", block.group(1)):
                    try:
                        matching |= urlsplit(url).hostname in hosts
                    except ValueError:
                        continue
            if not matching:
                errors.append(f"{identifier}: missing corresponding {category} source")
        claimed = re.findall(r"\b" + CASE_ID + r"\b", contents.get("Scenario coverage", ""))
        if len(claimed) != len(set(claimed)) or not claimed:
            errors.append(f"{identifier}: empty or duplicate scenario claims")
        declared_cases[identifier] = set(claimed)

    disk_guides = {path.resolve() for path in (root / "guides").rglob("*.md")}
    if disk_guides != set(module_paths.values()):
        errors.append("guide files and catalog paths do not match")
    startup_ids, expected_cases = registered_questions(startups, errors)
    case_ids: list[str] = []
    baseline: Counter = Counter()
    roles: dict[str, Counter] = defaultdict(Counter)
    mapped_cases: dict[str, set[str]] = defaultdict(set)
    for case in cases:
        if not isinstance(case, dict):
            errors.append("invalid scenario object")
            continue
        identifier, startup, role = case.get("id"), case.get("startup"), case.get("role")
        if not all(isinstance(value, str) and value for value in (identifier, startup, role, case.get("question"))):
            errors.append("scenario identity, startup, role and question must be nonempty strings")
            continue
        case_ids.append(identifier)
        if not re.fullmatch(CASE_ID, identifier) or startup not in startup_ids or not identifier.startswith(startup + "-"):
            errors.append(f"{identifier}: invalid startup association")
        status = case.get("baseline_status")
        if identifier in BASELINE_CASES:
            roles[startup][role] += 1
            if not isinstance(status, str) or status not in BASELINE_COUNTS:
                errors.append(f"{identifier}: invalid baseline status")
            else:
                baseline[status] += 1
        else:
            if "baseline_status" not in case or status is not None:
                errors.append(f"{identifier}: extension question must use baseline_status null")
        targets = case.get("guides")
        if not isinstance(targets, list) or not targets or not all(isinstance(item, str) for item in targets):
            errors.append(f"{identifier}: missing or invalid guide mapping")
            continue
        if len(targets) != len(set(targets)):
            errors.append(f"{identifier}: duplicate guide mapping")
        for target in targets:
            if target not in module_paths:
                errors.append(f"{identifier}: unknown guide: {target}")
            mapped_cases[target].add(identifier)
    if not BASELINE_CASES.issubset(case_ids):
        errors.append("registry must retain all original 60 baseline question IDs")
    if len(case_ids) != len(set(case_ids)) or set(case_ids) != expected_cases:
        errors.append("registry must contain exactly its registered scenario IDs without duplicates")
    if baseline != BASELINE_COUNTS:
        errors.append(f"baseline counts changed: {dict(baseline)}")
    for startup in BASELINE_STARTUPS:
        if len(roles[startup]) != 3 or sorted(roles[startup].values()) != [2, 2, 2]:
            errors.append(f"{startup}: original baseline needs three roles with two questions each")
    for identifier in module_paths:
        if declared_cases.get(identifier, set()) != mapped_cases.get(identifier, set()):
            errors.append(f"{identifier}: scenario mapping and guide coverage differ")
    for relative in CORE_DOCS:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing core document: {relative}")
        else:
            documents[path] = path.read_text(encoding="utf-8")
    for path, text in documents.items():
        check_links(root, path, text, errors)
    example = read_object(root / "examples" / "result.example.json", errors)
    if example is not None and (
        example.get("mode") != "reference"
        or example.get("status") != "reference_only"
        or example.get("observed_at_utc") is not None
        or example.get("findings") != []
    ):
        errors.append("fictional reference example must not claim customer observations")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    registry = json.loads((root / "tests" / "scenarios.json").read_text(encoding="utf-8"))
    counts = Counter(module["status"] for module in catalog["modules"])
    print(
        f"PASS: {len(catalog['modules'])} guides; {len(registry['scenarios'])} questions; "
        f"{len(registry['startups'])} scenario groups ({len(BASELINE_CASES)} baseline questions)."
    )
    print("Guide statuses: " + ", ".join(f"{status}={counts[status]}" for status in sorted(GUIDE_STATUSES)) + ".")
    print("Local documentation checks only. No Azure calls or live-policy validation performed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
