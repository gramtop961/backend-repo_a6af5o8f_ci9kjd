from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Inquiry(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    budget: Optional[str] = None
    message: str = Field(..., min_length=5)
