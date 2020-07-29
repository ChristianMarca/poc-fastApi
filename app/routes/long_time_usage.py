from fastapi import APIRouter
from typing import Optional
import asyncio
from ..controllers.core.sum import add_plus_one
from ..pydatic_models.responses_models import FunctionExecutionNTimes

router = APIRouter()


@router.get("/long-time/times/{time}", response_model=FunctionExecutionNTimes)
async def get_response_after_long_time_request(time: int = 60, number: Optional[int] = 30):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, add_plus_one, number, time)
    return result
