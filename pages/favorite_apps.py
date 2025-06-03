import streamlit as st

st.set_page_config(
    page_title="My Favorite Apps",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('My Favorite Apps')

with open('pages/favorite_apps.md', 'r') as f:
    st.markdown(f.read())
