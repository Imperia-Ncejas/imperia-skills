# Patterns

## Preferred Pattern: Controlled business errors via InternalException

- Use `InternalException(ERROR_CODE.X)` for business-rule failures.
- Keep `ResponseEntity<T>` for successful responses only.

```csharp
if (entity == null)
    throw new InternalException(ERROR_CODE.NOT_FOUND);
```

## Anti-Pattern: Error payload in ResponseEntity

- Do not encode controlled business errors in `ResponseEntity<T>` as return values.

```csharp
return new ResponseEntity<MyDto>(null, ERROR_CODE.NOT_FOUND);
```

## Controller Validation Pattern

- Validate request-scoped business constraints in controllers.
- Throw informative `InternalException` messages with field context.

```csharp
if (request.Data.EndDate != null)
    throw new InternalException(
        ERROR_CODE.INVALID_FORMAT_DATE,
        "EndDate must be null for BY_VOLUME contracts");
```
