import streamlit as st

st.title('My Favorite Apps')


with open('favorite_apps.md', 'r') as f:
    st.markdown(f.read())
