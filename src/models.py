from pydantic import BaseModel
from typing import List, Optional

class TokenClaims(BaseModel):
    """Schema for token claims (PoC)."""
    sub: str
    scopes: List[str]
    exp: Optional[int] = None
    iat: Optional[int] = None
    issuer: Optional[str] = None
