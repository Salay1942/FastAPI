from typing import Optional
from pydantic import BaseModel

class param(BaseModel):
    fromDate: str
    toDate: str
    providerCode: str
