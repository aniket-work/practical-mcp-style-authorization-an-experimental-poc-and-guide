import jwt
from time import time

SECRET = "test-secret"


def create_token(sub: str = "user-1", scopes=None):
    if scopes is None:
        scopes = ["read"]
    payload = {"sub": sub, "scopes": scopes, "iat": int(time())}
    return jwt.encode(payload, SECRET, algorithm="HS256")


if __name__ == "__main__":
    print(create_token())
