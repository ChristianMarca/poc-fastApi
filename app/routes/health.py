from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_health_check():
    return {"status": 'UP'}
