from sqlalchemy import Column , Integer , String , Text , Enum as SQLENUM
from enum import Enum

class TodoStatus(Enum):
    IN_PROGRESS = "in_progress"
    DONE = "done"