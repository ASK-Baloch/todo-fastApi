from pydantic import BaseModel

# Request and Response Modal

class TodoCreate(BaseModel):
    content: str

    class Config:
        from_attributes = True
