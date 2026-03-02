---
name: company-skill-bootstrap
description: Standard workflow to propose, design, and publish reusable Codex skills for this company repository. Use when Codex needs to create or update a skill for multi-project reuse, define clear trigger descriptions, decide resource folders (scripts, references, assets), set agents/openai.yaml metadata, and prepare review-ready changes.
---

# Company Skill Bootstrap

## Overview

Create or update skills in this repository with consistent structure and quality so teams can reuse them across projects.

## Required Output

For each skill task, produce:

1. Skill folder in `skills/` using lowercase hyphen-case
2. `SKILL.md` with frontmatter (`name`, `description`) and imperative instructions
3. `agents/openai.yaml` with `display_name`, `short_description`, `default_prompt`
4. Only required resource folders (`scripts/`, `references/`, `assets/`)

## Workflow

### 1. Capture request with concrete examples

- Ask for at least three example prompts that should trigger the skill.
- Confirm target users, expected outputs, and project constraints.
- If examples are missing, infer a first version and mark assumptions.

### 2. Design reusable resources

- Add `scripts/` only for deterministic repeated operations.
- Add `references/` for long or domain-specific material.
- Add `assets/` only for files copied into deliverables.
- Keep `SKILL.md` lean and link detailed content from `references/`.

### 3. Author metadata and instructions

- Write `name` in lowercase hyphen-case, max 64 characters.
- Write `description` with both capability and trigger context.
- Use imperative voice in body instructions.
- Keep trigger logic in frontmatter description, not in body sections.

### 4. Set UI metadata

- Keep `agents/openai.yaml` minimal:
- `interface.display_name`
- `interface.short_description` (25 to 64 characters)
- `interface.default_prompt` that mentions `$skill-name`
- Add icons or brand color only when explicitly requested.

### 5. Review before merge

- Validate naming, frontmatter, and required files.
- Remove placeholder files that are not needed.
- Remove duplicated content across `SKILL.md` and `references/`.
- Include at least one realistic usage example in the skill content.

## Quality Bar

- Optimize for reuse across projects, not one-off tasks.
- Prefer small deterministic scripts over repeated ad hoc code.
- Add precise guardrails for fragile workflows; keep flexible workflows concise.
- Keep skill folders self-contained without extra docs like `README.md` or `CHANGELOG.md`.

## References

- Read `references/intake-template.md` during discovery and scoping.
- Read `references/review-checklist.md` before opening or approving a pull request.
