import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import base64
from style import main_style
from streamlit_pdf_viewer import pdf_viewer

# Page configuration
st.set_page_config(
    page_title="John Feng's Portfolio Site",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
# st.markdown(main_style, unsafe_allow_html=True)

# Header Section
cols = st.columns([4, 1])
with cols[1]:
    st.image(Image.open(r'assets/Linkedin_pic_cropped.jpg'), )
with cols[0]:
    st.markdown("""
        <div class="profile-section">
            <h1 style="text-align: center; ">John Feng</h1>
            <h2 style="text-align: center; color: lightgray">Applied Scientist | Data Scientist | AI Engineer</h2>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<h2 class="section-title">👨‍🔬 About Me</h2>', unsafe_allow_html=True)
st.markdown("""
I am a physicist turned data scientist and software developer with expertise in machine learning and
data science. I love solving complex problems and creating 
innovative solutions that make a difference. I also like to make pretty plots and apps. """, unsafe_allow_html=True)

with st.expander("📈 **Resume for Data Science/AI Engineer**"):
    # st.markdown(open("RESUME/resume_data_ai.md", encoding='utf-8').read(),
    #             unsafe_allow_html=True)
    pdf_viewer(open("RESUME/John-Feng-AI-Engineer-Resume.pdf", "rb").read())
st.download_button(label="Download Resume 🔽", data=open("RESUME/John-Feng-AI-Engineer-Resume.pdf", "rb").read(), file_name="John-Feng-AI-Engineer-Resume.pdf")

with st.expander("🔬 **Resume for Hard Tech**"):
    # st.markdown(open("RESUME/resume_hard_tech.md", encoding='utf-8').read(),
    #             unsafe_allow_html=True)
    pdf_viewer(open("RESUME/John Feng Resume Hard Tech 2025-03-08.pdf", "rb").read())
st.download_button(label="Download Resume 🔽", data=open("RESUME/John Feng Resume Hard Tech 2025-03-08.pdf", "rb").read(), file_name="John Feng Resume Hard Tech 2025-03-08.pdf")
# Projects Section
st.markdown('<h2 class="section-title">📊 Projects  </h2>', unsafe_allow_html=True)
projects = [
    {
        'title': '**Detector Frame-by-Frame Analysis Dashboard**',
        'description': 'A dashboard that allows users to analyze detector data frame-by-frame',
        'technologies': ['Python', 'Streamlit', 'Pandas', 'Plotly'],
        'link': 'https://frame-analyzer.streamlit.app/',
        'gif': 'assets/frame-by-frame.gif'
    },
    {
        'title': '**Pixel and Spectrum Analysis of Gamma-Ray Detector Data with Moving Mask**',
        'description': 'This app allows users to analyze pixel and spectrum of gamma-ray detector data. The data is processed for each moving mask position to expose small areas of interest. The spectrum is calculated for each pixel and displayed in a spectrum plot.',
        'technologies': ['Python', 'Streamlit', 'Pandas', 'Plotly'],
        'link': 'https://johnfeng-spectrum-analyzer.streamlit.app/',
        'gif': 'assets/Spectrum-analyzer.gif'
    },
    {
        'title': '**PrepPal - AI-Powered English Exam Prep**',
        'description': 'Winner of 2023 Brave AI Accelerator Hackathon. A web app that uses AI to help users prepare for English proficiency exams such as IELTS and TOEFL. The app generates writing and reading practice questions and provides instant feedback.',
        'technologies': ['Python', 'Streamlit', 'OpenAI', 'LangChain'],
        'link': 'https://preppal.streamlit.app/',
        'gif': 'assets/PrepPal_logo.jpeg'
    }
]

for project in projects:
    with st.expander(project['title'], expanded=True):
        st.write(project['description'])
        st.write("**Tech Stack:** " + ", ".join(project['technologies']))
        st.markdown(f"**Deployed App:** [{project['link']}]({project['link']})")
        st.caption("*Note: This project is currently hosted on Streamlit Cloud, which may take a few seconds to load.")
        gif_path = project['gif']
        if gif_path.lower().endswith(('.jpg', '.jpeg')):
            image = Image.open(gif_path)
            st.image(image, use_column_width=True)
        else:
            st.image(gif_path)

# Contact Section
st.markdown('<h2 class="section-title">Contact</h2>', unsafe_allow_html=True)
contact_col1, contact_col2 = st.columns(2)
with contact_col1:
    st.markdown("""
    ### Get in Touch
    - 📧 Email: johnfengphd@gmail.com
    - 📱 Phone: (647) 716 7981
    - 📍 Location: 
        * Toronto, ON, Canada
        * Victoria, BC, Canada
    """)

with contact_col2:
    st.markdown("""
    ### Links
    - [LinkedIn](https://www.linkedin.com/in/john-feng-5735321b8/)
    - [GitHub](https://github.com/johnnykfeng)
    """)

# Footer
st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #7f8c8d;">
        © 2025 John Feng. All rights reserved.
    </div>
""", unsafe_allow_html=True)
