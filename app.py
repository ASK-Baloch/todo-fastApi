import requests
import streamlit as st

# Define the base URL of your FastAPI app
BASE_URL = "http://localhost:8000"
 
def get_todos():
    response = requests.get(BASE_URL)
    return response.json()

def create_todo(content):
    response = requests.post(BASE_URL, json={"content": content})
    return response.json()

def update_todo(todo_id):
    response = requests.put(f"{BASE_URL}/{todo_id}")
    return response.json()

def delete_todo(todo_id):
    response = requests.delete(f"{BASE_URL}/{todo_id}")
    return response.json()

# Streamlit UI
def main():
    st.title("FastAPI Todo App")

    # Display existing todos
    todos = get_todos()
    st.write("## Todos")
    for todo in todos:
        st.write(f"{todo['id']}. {todo['content']} - Status: {todo['status']}")

    # Create a new todo
    st.write("## Create Todo")
    new_todo_content = st.text_input("Enter new todo content:")
    if st.button("Create Todo"):
        created_todo = create_todo(new_todo_content)
        st.success(f"Todo created: {created_todo['content']}")
        st.rerun()

    # Update a todo
    st.write("## Update Todo Status")
    update_todo_id = st.number_input("Enter todo ID to update:")
    if st.button("Update Todo Status"):
        updated_todo = update_todo(update_todo_id)
        st.success(f"Todo updated - New status: {updated_todo['status']}")
        st.rerun()

    # Delete a todo
    st.write("## Delete Todo")
    delete_todo_id = st.number_input("Enter todo ID to delete:")
    if st.button("Delete Todo"):
        deleted_todo = delete_todo(delete_todo_id)
        st.success(f"Todo deleted: {deleted_todo['message']}") 
        st.rerun()

if __name__ == "__main__":
    main()
