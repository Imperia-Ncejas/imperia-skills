#!/usr/bin/env python3
"""
Minimal repository validator for Imperia skills.

Checks:
- Every skill folder under skills/*/* has SKILL.md and agents/openai.yaml
- SKILL.md frontmatter includes name and description
- Skill name uses lowercase hyphen-case and <= 64 chars
- openai.yaml contains interface display_name and short_description
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


MAX_NAME_LEN = 64
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"

    if not skill_md.exists():
        errors.append(f"{skill_dir}: missing SKILL.md")
        return errors

    if not openai_yaml.exists():
        errors.append(f"{skill_dir}: missing agents/openai.yaml")

    frontmatter = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    name = frontmatter.get("name", "").strip()
    description = frontmatter.get("description", "").strip()

    if not name:
        errors.append(f"{skill_dir}: SKILL.md frontmatter missing name")
    elif len(name) > MAX_NAME_LEN or not NAME_PATTERN.match(name):
        errors.append(f"{skill_dir}: invalid name '{name}'")

    if not description:
        errors.append(f"{skill_dir}: SKILL.md frontmatter missing description")

    if openai_yaml.exists():
        content = openai_yaml.read_text(encoding="utf-8")
        if "interface:" not in content:
            errors.append(f"{skill_dir}: openai.yaml missing interface section")
        if "display_name:" not in content:
            errors.append(f"{skill_dir}: openai.yaml missing interface.display_name")
        if "short_description:" not in content:
            errors.append(f"{skill_dir}: openai.yaml missing interface.short_description")

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    skills_root = repo_root / "skills"
    if not skills_root.exists():
        print("ERROR: skills/ folder not found")
        return 1

    errors: list[str] = []
    for domain_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
        for skill_dir in sorted(p for p in domain_dir.iterdir() if p.is_dir()):
            errors.extend(validate_skill(skill_dir))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation succeeded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
