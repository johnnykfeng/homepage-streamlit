import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import base64
from style import main_style

# Page configuration
st.set_page_config(
    page_title="John Feng's Portfolio Site",
    page_icon="🚀",
    layout="wide"
)
with st.sidebar:
    st.subheader("Favorite apps")
    st.markdown("""
    - [My Favorite Apps](favorite_apps.py)
    """)

# Custom CSS
# st.markdown(main_style, unsafe_allow_html=True)

# # Display profile picture
# try:
#     profile_image = Image.open(r'assets/Linkedin_pic_cropped.jpg')
#     col1, col2, col3 = st.columns([1,2,1])
#     with col2:
#         st.image(profile_image, width=300, caption='John Feng')
# except FileNotFoundError:
#     st.warning("Profile image not found in assets folder")

# Header Section
cols = st.columns([4,1])
with cols[1]:
    st.image(Image.open(r'assets/Linkedin_pic_cropped.jpg'), )
with cols[0]:
    st.markdown("""
        <div class="profile-section">
            <h1 style="text-align: center; ">John Feng</h1>
            <h2 style="text-align: center; color: lightgray">Applied Scientist | Data Scientist | AI Engineer</h2>
        </div>
    """, unsafe_allow_html=True)

# About Me Section
# cols = st.columns([1,1,1])
# with cols[0]:
#     st.image(Image.open(r'assets/Linkedin_pic_cropped.jpg'), 
#              width=75)
# with cols[1]:
st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    I am a passionate data scientist and software developer with expertise in machine learning, 
    data analysis, and full-stack development. I love solving complex problems and creating 
    innovative solutions that make a difference.""", unsafe_allow_html=True)
    
    st.subheader("Education")
    st.markdown("""
    - PhD in Physics, University of Toronto
    - MSc and BA in Physics, University of Toronto
    """)
    
    st.subheader("Experience")
    st.markdown("""
    #### Applied Scientist in Detector Physics, Redlen Technologies (Oct 2023-Present)
    """)

# Skills Section
st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)
skills = {
    'Programming Languages': ['Python', 'R', 'JavaScript', 'SQL'],
    'Data Science': ['Machine Learning', 'Deep Learning', 'Data Visualization', 'Statistical Analysis'],
    'Web Development': ['Streamlit', 'React', 'Node.js', 'Django'],
    'Tools & Technologies': ['Git', 'Docker', 'AWS', 'TensorFlow', 'PyTorch']
}

for category, skill_list in skills.items():
    st.markdown(f"### {category}")
    st.write(", ".join(skill_list))

# Projects Section
st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)
projects = [
    {
        'title': 'Detector Frame-by-Frame Analysis Dashboard',
        'description': 'A dashboard that allows users to analyze detector data frame-by-frame',
        'technologies': ['Python', 'Streamlit', 'Pandas', 'Plotly'],
        'link': 'https://frame-analyzer.streamlit.app/'
    },
    {
        'title': 'Pixel and Spectrum Analysis of Gamma-Ray Detector Data with Moving Mask',
        'description': 'This app allows users to analyze pixel and spectrum of gamma-ray detector data. The data is processed for each moving mask position to expose small areas of interest. The spectrum is calculated for each pixel and displayed in a spectrum plot.',
        'technologies': ['Python', 'Streamlit', 'Pandas', 'Plotly'],
        'link': 'https://johnfeng-spectrum-analyzer.streamlit.app/'
    }
]

for project in projects:
    with st.expander(project['title']):
        st.write(project['description'])
        st.write("**Technologies:** " + ", ".join(project['technologies']))
        st.markdown(f"[View Project]({project['link']})")

# Contact Section
st.markdown('<h2 class="section-title">Contact</h2>', unsafe_allow_html=True)
contact_col1, contact_col2 = st.columns(2)
with contact_col1:
    st.markdown("""
    ### Get in Touch
    - 📧 Email: johnfengphd@gmail.com
    - 📱 Phone: (647) 716 7981
    - 📍 Location: Toronto, ON, Canada
    """)

with contact_col2:
    st.markdown("""
    ### Social Media
    - [LinkedIn](https://linkedin.com/in/yourprofile)
    - [GitHub](https://github.com/yourusername)
    - [Twitter](https://twitter.com/yourhandle)
    """)

# Footer
st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #7f8c8d;">
        © 2024 Your Name. All rights reserved.
    </div>
""", unsafe_allow_html=True)
