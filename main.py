from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/todos")
def get_todos():
    return {"todos": [{"id":1, "content":"Wash the dishes"}]}