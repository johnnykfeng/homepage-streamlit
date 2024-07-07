import streamlit as st

st.title('John Feng Home Page')


with open('favorite_apps.md', 'r') as f:
    st.markdown(f.read())
