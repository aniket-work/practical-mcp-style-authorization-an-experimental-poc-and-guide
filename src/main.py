from fastapi import FastAPI, Request, HTTPException
from .auth import decode_token
from .policy import is_allowed

app = FastAPI(title="MCP-Style Auth PoC")

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    auth = request.headers.get("authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")

    token = auth.split(None, 1)[1]
    try:
        claims = decode_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    if not is_allowed(claims, request.url.path, request.method):
        raise HTTPException(status_code=403, detail="Access denied")

    request.state.claims = claims
    return await call_next(request)

@app.get("/resources")
async def get_resources(request: Request):
    return {"data": ["resource-1", "resource-2"], "subject": request.state.claims.sub}

@app.get("/admin")
async def admin_panel(request: Request):
    return {"admin": True, "subject": request.state.claims.sub}
