import streamlit as st

st.title("My To-Do App")

if "todos" not in st.session_state:
    st.session_state.todos = []

todo = st.text_input("Type in to-do")

if st.button("Add"):
    if todo:
        st.session_state.todos.append(todo)

st.write("### Tasks")
st.write(st.session_state.todos)
