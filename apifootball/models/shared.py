from typing import Any, Dict

from pydantic import BaseModel


class ResponseWrapper(BaseModel):
    get: str
    parameters: Dict[str, Any]
    errors: list
    results: int
    paging: Dict[str, int]
