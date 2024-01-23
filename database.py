from typing import List
from pydantic import BaseModel

class TaskInDB(BaseModel):
    id: int
    title: str
    description: str
    status: bool

tasks_db: List[TaskInDB] = []
task_id_counter = 1
