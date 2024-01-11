from sqlalchemy import Column , Integer , DateTime ,  String , Text , Enum as SQLENUM
from sqlalchemy.sql import func
from enum import Enum
from database import Base


class TodoStatus(Enum):
    IN_PROGRESS = "in_progress"
    DONE = "done"

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer , primary_key = True , index = True)
    created_at = Column(DateTime(timezone = True) , server_default = func.now())
    content = Column(Text)
    image = Column(String(255))
    status = Column(SQLENUM(TodoStatus), index=True , default=TodoStatus.IN_PROGRESS)

    def __repr__(self):
        return f"<Todo(id={self.id}, created={self.created_at}, status={self.status.value}, content={self.content})>"