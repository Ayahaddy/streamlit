import streamlit as st

st.header("This is a button")

if st.button("Say Hello!"):
    st.write("Hello!")
else:
    st.write("See you!")