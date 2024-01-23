from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: str
    description: str
    status: bool

class TaskResponse(TaskCreate):
    id: int
    status: bool

class ErrorResponse(BaseModel):
    detail: str
