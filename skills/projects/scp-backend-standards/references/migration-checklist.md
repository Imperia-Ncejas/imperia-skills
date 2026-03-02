# Migration Checklist

Use this checklist when refactoring code to this convention.

## Detection

- Find methods returning `ResponseEntity<T>` with error code values.
- Find null checks or business validations returning error payloads.

## Refactor

- Replace each controlled business-error return with `InternalException`.
- Keep success return unchanged.
- Preserve existing error code semantics.

## Validation

- Add controller-level checks for request-specific business rules.
- Improve messages with field + condition.

## Review

- Confirm no endpoint still returns controlled errors in `ResponseEntity`.
- Confirm new exceptions map to expected HTTP behavior in middleware/filter.
- Confirm PR summary includes touched endpoints and non-migrated edge cases.
