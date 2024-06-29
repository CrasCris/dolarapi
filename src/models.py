from typing import Dict
from pydantic import BaseModel

class Serie(BaseModel):
    Serie: Dict[str, str]