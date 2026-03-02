# Governance

## Purpose

Maintain a consistent quality bar for all company skills.

## Contribution Rules

1. Place each skill in the correct domain folder under `skills/`.
2. Include `SKILL.md` and `agents/openai.yaml` in every skill.
3. Keep shared templates in repository root `references/`.
4. Keep project-specific constraints in `skills/projects/`.
5. Avoid duplicating long reference content across files.

## Review Process

1. Validate structure and metadata.
2. Review trigger quality and activation clarity.
3. Review output contract completeness.
4. Confirm no cross-project leakage for project-specific skills.

## Versioning

- Update `VERSION` for every released set of governance-compatible changes.
- Document notable changes in `CHANGELOG.md`.
