from fastapi import APIRouter
from typing import Optional
import asyncio
from ..controllers.core.create_huge_list import run_create_huge_list_for_n_seconds
from ..pydatic_models.responses_models import FunctionExecutionNTimes

router = APIRouter()


@router.get("/array/times/{time}", response_model=FunctionExecutionNTimes)
async def get_response_after_high_memory_usage(time: int = 60, data_slot: Optional[int] = 30):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, run_create_huge_list_for_n_seconds, data_slot, time)
    return result
