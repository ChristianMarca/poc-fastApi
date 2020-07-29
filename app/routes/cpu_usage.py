from fastapi import APIRouter
from typing import Optional
import asyncio
from ..controllers.core.fibonachi_test import run_fib_for_n_seconds
from ..pydatic_models.responses_models import FunctionExecutionNTimes

router = APIRouter()


@router.get("/usage", response_model=FunctionExecutionNTimes)
async def get_response_after_high_cpu_usage(max_number_fibo: Optional[int] = 100, time_on_execution: Optional[int] = 30):
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, run_fib_for_n_seconds, max_number_fibo, time_on_execution)
    return result
