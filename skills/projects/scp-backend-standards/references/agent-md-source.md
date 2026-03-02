# Agent MD Source

Source notes captured for this skill:

- Use `InternalException` for business logic errors.
- Avoid returning controlled errors through `ResponseEntity` when standard exception mapping is expected.
- Keep controllers POST-only.
- Use `SCPRequest<T>` with `User` and `Data`.
- Keep business logic in Models.
- Keep DTOs as pure data structures.

Use this file as the canonical source snapshot when updating this skill from future `agent.md` revisions.
