from typing import Optional

from pydantic import BaseModel


class Suggestion(BaseModel):
    value: str
    unrestricted_value: str
    data: dict[str, Optional[str]]
