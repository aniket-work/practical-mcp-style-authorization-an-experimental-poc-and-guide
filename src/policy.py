from .models import TokenClaims

RESOURCE_SCOPE_MAP = {
    "/admin": ["admin"],
    "/resources": ["read", "write"],
}


def is_allowed(claims: TokenClaims, path: str, method: str) -> bool:
    """Very small policy evaluator: require any overlap between token scopes and resource scopes."""
    required = RESOURCE_SCOPE_MAP.get(path, [])
    return any(scope in claims.scopes for scope in required)
