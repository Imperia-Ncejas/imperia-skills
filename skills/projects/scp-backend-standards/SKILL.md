---
name: scp-backend-standards
description: SCP Backend project standards. Use when implementing or reviewing SCP backend endpoints/controllers/models/DTOs, SCPRequest<T> request payloads, InternalException error handling, POST-only controllers, and SCP-specific folder/module conventions. Trigger on requests mentioning SCP Backend, SCPRequest, InternalException, controller endpoints, or production/prod branch changes.
---

# SCP Backend Standards

## Authority
If there is a conflict, follow `docs/decisions.md` (authoritative execution state).

## When to use
Use this skill when working on the SCP Backend repository, especially when:
- creating or refactoring API endpoints/controllers
- defining request/response payload patterns
- handling business-rule errors
- aligning code to SCP-specific folder/module conventions

## SCP API & Controller conventions
- Controllers must expose **POST endpoints only**.
- Requests must use `SCPRequest<T>` payloads that carry `User` and `Data`.
- Controllers should:
  - validate request data / contract-specific business rules (when appropriate),
  - configure context,
  - generate tokens,
  - delegate business logic to Models.

## Error handling (SCP-specific)
- Use `InternalException` for business logic errors (do not return error codes via ResponseEntity when the intended behavior is a BadRequest/standard error mapping).
- Prefer informative messages when throwing for validation errors.

## Models / DTO conventions (SCP-specific emphasis)
- Models contain all business logic and DB operations.
- DTOs are pure data structures: no business logic; initialize collections as empty; use nullable types for optional fields.

## Output contract
When reviewing code/diffs, return:
1) **Summary** (bullets)
2) **Violations** with:
   - file, symbol (class/method), rule, severity (BLOCKER/MAJOR/MINOR), why, concrete fix
3) If asked to propose changes: **patch** limited to the touched areas; do not change behavior unless explicitly requested.

## References
See:
- `references/agent-md-source.md` (project standards source material)
- `references/endpoint-template.md` (SCP endpoint skeleton)
- `references/patterns.md` (error handling and validation patterns)
- `references/migration-checklist.md` (migration and review checklist)
