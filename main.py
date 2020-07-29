from fastapi import FastAPI, Header, HTTPException
from app.routes import cpu_usage, memory_usage, long_time_usage, health

app = FastAPI()


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

app.include_router(
    cpu_usage.router,
    prefix="/cpu",
    tags=["cpu"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    long_time_usage.router,
    prefix="/time",
    tags=["time"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    memory_usage.router,
    prefix="/memory",
    tags=["memory"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    health.router,
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)
