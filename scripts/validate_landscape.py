from __future__ import annotations

from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_PATH = ROOT / "data" / "projects.yaml"
ASSESSMENTS_PATH = ROOT / "data" / "project-assessments.yaml"

PROJECT_REQUIRED = ("name", "category", "domain", "url", "relation")
ASSESSMENT_REQUIRED = (
    "name",
    "type",
    "strengths",
    "weaknesses",
    "relation_to_opensciflow",
    "contact_priority",
)
CONTACT_PRIORITIES = {"high", "medium", "low"}


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a mapping")
    return data


def require_nonempty_string(value: object, field: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be a non-empty string")


def validate_url(value: object, field: str, errors: list[str]) -> None:
    require_nonempty_string(value, field, errors)
    if not isinstance(value, str):
        return
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        errors.append(f"{field} must be an http(s) URL")


def validate_items(items: object, required: tuple[str, ...], label: str) -> tuple[list[dict], list[str]]:
    errors: list[str] = []
    if not isinstance(items, list):
        return [], [f"{label} must be a list"]

    valid_items: list[dict] = []
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{label}[{index}] must be an object")
            continue
        valid_items.append(item)
        for field in required:
            if field not in item:
                errors.append(f"{label}[{index}] missing {field}")
                continue
            if field == "url":
                validate_url(item[field], f"{label}[{index}].{field}", errors)
            else:
                require_nonempty_string(item[field], f"{label}[{index}].{field}", errors)

    names = [item.get("name") for item in valid_items if isinstance(item.get("name"), str)]
    for name, count in sorted(Counter(names).items()):
        if count > 1:
            errors.append(f"{label} contains duplicate name {name!r}")

    return valid_items, errors


def main() -> None:
    projects_data = load_yaml(PROJECTS_PATH)
    assessments_data = load_yaml(ASSESSMENTS_PATH)

    projects, errors = validate_items(projects_data.get("projects"), PROJECT_REQUIRED, "projects")
    assessments, assessment_errors = validate_items(
        assessments_data.get("assessments"),
        ASSESSMENT_REQUIRED,
        "assessments",
    )
    errors.extend(assessment_errors)

    project_names = {item["name"] for item in projects if isinstance(item.get("name"), str)}
    assessment_names = {item["name"] for item in assessments if isinstance(item.get("name"), str)}

    for missing in sorted(project_names - assessment_names):
        errors.append(f"missing assessment for project {missing!r}")
    for unknown in sorted(assessment_names - project_names):
        errors.append(f"assessment references unknown project {unknown!r}")

    for item in assessments:
        priority = item.get("contact_priority")
        if priority not in CONTACT_PRIORITIES:
            errors.append(f"assessment {item.get('name')!r} has invalid contact_priority {priority!r}")

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"Validated {len(projects)} projects and {len(assessments)} assessments")


if __name__ == "__main__":
    main()

