# SCP Endpoint Template

```csharp
[ApiController]
[Route("api/[controller]")]
public class ContractsController : ControllerBase
{
    [HttpPost("get-single")]
    public async Task<ResponseEntity<SupplierContractDTO>> GetSingle(
        [FromBody] SCPRequest<GetSingleContractRequestDTO> request)
    {
        // 1) Validate request-specific business rules
        if (request.Data.EndDate != null)
            throw new InternalException(
                ERROR_CODE.INVALID_FORMAT_DATE,
                "EndDate must be null for BY_VOLUME contracts");

        // 2) Configure context / security tokens if required
        // context.Configure(request.User);
        // tokenService.Generate(request.User);

        // 3) Delegate business logic to model/service
        return await ContractModel.GetSingleContract(_context, request.Data.Id);
    }
}
```

Notes:

- Keep controllers focused on orchestration and validation.
- Keep business logic and DB operations in Models.
- Throw `InternalException` for controlled business failures.
