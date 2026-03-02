# Skill Review Checklist

Run this checklist before merge.

## Frontmatter

- `SKILL.md` includes only `name` and `description`.
- `name` is lowercase hyphen-case and <= 64 chars.
- `description` explains what the skill does and when it should trigger.

## Structure

- `agents/openai.yaml` exists and includes:
- `interface.display_name`
- `interface.short_description` (25 to 64 chars)
- `interface.default_prompt` mentioning `$skill-name`
- Resource folders exist only if they are used.

## Content Quality

- Instructions use imperative voice.
- Trigger logic is in frontmatter description, not in body sections.
- `SKILL.md` does not duplicate long content from `references/`.
- At least one realistic usage example is included.

## Operational Quality

- Added scripts were executed at least once.
- Placeholder files were removed.
- Naming and paths are consistent with repository conventions.
