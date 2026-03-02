# Imperia Skills

Central repository for reusable Codex skills used across Imperia projects.

## Current Structure

```text
IMPERIA-SKILLS/
  references/
    intake-template.md
    output-contracts.md
    review-checklist.md

  skills/
    core/
      company-skill-bootstrap/

    backend-csharp/
      clean-code-csharp/
      error-handling-validation/
      efcore-patterns/

    frontend-angular/
      angular-architecture/
      angular-code-style/

    shared/
      pr-review-diff/
      release-notes/

    qa-product/
      feature-qna/

    projects/
      scp-backend-standards/

  tooling/
  CHANGELOG.md
  GOVERNANCE.md
  OWNERS.yaml
  README.md
  VERSION
```

## Skill Domains

- `skills/core/`: meta-skills to create and improve skills.
- `skills/backend-csharp/`: backend C# standards and engineering patterns.
- `skills/frontend-angular/`: Angular architecture and style standards.
- `skills/shared/`: transversal workflows reused across teams.
- `skills/qa-product/`: product and functional QA assistance skills.
- `skills/projects/`: project-specific skills that must not leak to other repos.

## Shared References

- `references/intake-template.md`: intake template for new skills.
- `references/review-checklist.md`: review gates before merge.
- `references/output-contracts.md`: standard response/output contracts.

## Contribution Rules

1. Create or update skills under `skills/<domain>/<skill-name>/`.
2. Keep names in lowercase hyphen-case.
3. Include `SKILL.md` and `agents/openai.yaml` in each skill.
4. Keep global reusable docs in `references/`.
5. Run `tooling/validate_skills.py` before opening a PR.
