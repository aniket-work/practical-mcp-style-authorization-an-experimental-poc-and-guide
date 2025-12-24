import jwt
from jwt import PyJWTError
from .models import TokenClaims
from typing import Any

# PoC symmetric secret - replace with env / key management in real systems
SECRET = "test-secret"


def decode_token(token: str) -> TokenClaims:
    """Decode and validate a JWT token into TokenClaims.

    Raises ValueError on invalid tokens.
    """
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])  # PoC: symmetric key
        return TokenClaims(**payload)
    except PyJWTError as e:
        raise ValueError("Invalid token") from e
