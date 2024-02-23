import streamlit as st
from modules import functionsd14

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functionsd14.write_todos(todos)


todos = functionsd14.get_todos()

st.title("My Todo App")
st.subheader("This is a to-do app")   # order matters
st.write("It aims to keep you organised and productive")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox: # checkbox equates to a T/F value
        todos.pop(index)
        functionsd14.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add new todo ....",
              on_change=add_todo,key='new_todo')





# session state is like a  dictionary
# it's its own type, a type of streamlit
# the key is 'new_todo' and the value is the to_do;
# we enter in the textbox
# this script is executed followed
# by the function call add_todo()
# (on_change argument-action-callback fn)
# everytime we enter;
# something in the textbox
# todos.txt will also be updated
# checkbox is added to the web app
# checkbox can also have a key, hence
# it is also a part of the session state object
# the value for the respective;
# checkbox keys will be set to true if checked

