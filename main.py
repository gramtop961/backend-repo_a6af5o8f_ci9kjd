import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

app = FastAPI(title="Video Editor Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Inquiry(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    budget: Optional[str] = None
    message: str = Field(..., min_length=5)

@app.get("/")
def read_root():
    return {"message": "Portfolio API running"}

@app.post("/inquiry")
def create_inquiry(inquiry: Inquiry):
    # In a real app we would persist to DB or send email. For now, echo back.
    return {"status": "ok", "received": inquiry.model_dump()}

@app.get("/test")
def test_database():
    """Basic backend status endpoint"""
    return {"backend": "running"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
