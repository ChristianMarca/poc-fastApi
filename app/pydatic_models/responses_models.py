from pydantic import BaseModel


class FunctionExecutionNTimes(BaseModel):
    iteration_number: str
    time: float
    used_memory: float = 0
