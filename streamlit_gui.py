import streamlit as st

st.title("My To-Do App")

todo = st.text_input("Type in to-do")

if st.button("Add"):
    if "todos" not in st.session_state:
        st.session_state.todos = []
    st.session_state.todos.append(todo)

st.write("### Tasks")
st.write(st.session_state.get("todos", []))
