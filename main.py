from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database import get_db
from app.schemas.todo import TodoCreate 
from app.models.todo import Todo , TodoStatus

app = FastAPI()

@app.get("/api/v1/todos")
def get_todos(db:Session = Depends(get_db)):
    return db.query(Todo).all()

@app.get("/api/v1/todos/{todo_id}")
def get_todo( todo_id:int , db:Session = Depends(get_db)):
    return db.query(Todo).filter(Todo.id == todo_id).first()   

@app.put("/api/v1/todos/{todo_id}")
def update_todo( todo_id:int , db:Session = Depends(get_db)):
    try:
        todo =  db.query(Todo).filter(Todo.id == todo_id).first()   

        if todo is None:
            return None
        
        if todo.status == TodoStatus.IN_PROGRESS:
            todo.status = TodoStatus.DONE
        else:
            todo.status = TodoStatus.IN_PROGRESS
        
        db.commit()
        db.refresh(todo)
        return todo       
    except SQLAlchemyError as e:
        #log for production in future
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Error while updating todo")
    except Exception as e:
        #log for production in future
        print(e)
        raise HTTPException(status_code=500, detail="UnExpected Error Occured")
    
@app.delete("/api/v1/todos/{todo_id}")
def delete_todo( todo_id:int , db:Session = Depends(get_db)):
    try:
        todo =  db.query(Todo).filter(Todo.id == todo_id).first()   

        if todo is None:
            return None
        db.delete(todo)
        db.commit()
        return {"message" : f"Deleted the todo  {todo_id }"}       
    except SQLAlchemyError as e:
        #log for production in future
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Error while deleting todo")
    except Exception as e:
        #log for production in future
        print(e)
        raise HTTPException(status_code=500, detail="UnExpected Error Occured")

@app.post("/api/v1/todos")
def create_todo(todo_request: TodoCreate , db:Session = Depends(get_db)):
    try:
        new_todo = Todo(content = todo_request.content)
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return new_todo  
    except SQLAlchemyError as e:
        #log for production in future
        print(e)
        db.rollback()
        raise HTTPException(status_code=500, detail="Error while creating todo")
    except Exception as e:
        #log for production in future
        print(e)
        raise HTTPException(status_code=500, detail="UnExpected Error Occured")