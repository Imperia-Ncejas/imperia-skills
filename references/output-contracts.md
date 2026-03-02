# Output Contracts

Use these contracts to keep skill responses consistent and reviewable.

## Default Contract for Skill-Creation Tasks

When a skill-creation workflow runs, return:

1. Folder structure proposal (tree format)
2. Draft `SKILL.md` content
3. `agents/openai.yaml` content (if required)
4. Recommended trigger description
5. Review checklist confirmation

## Optional Contract Extensions

- Add implementation notes when migrations are required.
- Add validation output summary when scripts are executed.
- Add risk flags for assumptions or missing context.
