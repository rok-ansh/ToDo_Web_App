import streamlit as st
import functions

todos = functions.web_get_todos()


def add_todo():
    todo = st.session_state["new_todo"]

    todos.append(todo + "\n")
    functions.web_write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox==True:
        todos.pop(index)
        functions.web_write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add new todo ....", on_change=add_todo, key='new_todo')

#
# # print("Hello")
# st.session_state