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
def local_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", 
                    unsafe_allow_html=True)

local_css("style.css")


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

st.markdown('<h2 class="section-title">👨‍🔬 About Me</h2>',
            unsafe_allow_html=True)
st.markdown("""
Started as a physicist, with training in data science and software development, and a passion for building machine learning and AI applications. I love solving complex problems and creating 
innovative solutions that make a difference.

Built a few AI applications, including a web app for English exam preparation and a dashboard for analyzing detector data.
""", 
unsafe_allow_html=True)

with st.expander("📈 **Resume for Data Science/AI Engineer**"):
    # st.markdown(open("RESUME/resume_data_ai.md", encoding='utf-8').read(),
    #             unsafe_allow_html=True)
    pdf_viewer(open("RESUME/John-Feng-AI-Engineer-Resume.pdf", "rb").read())
st.download_button(label="Download Resume 🔽", data=open(
    "RESUME/John-Feng-AI-Engineer-Resume.pdf", "rb").read(), file_name="John-Feng-AI-Engineer-Resume.pdf")

with st.expander("🔬 **Resume for Hard Tech**"):
    # st.markdown(open("RESUME/resume_hard_tech.md", encoding='utf-8').read(),
    #             unsafe_allow_html=True)
    pdf_viewer(
        open("RESUME/John Feng Resume Hard Tech 2025-03-08.pdf", "rb").read())
st.download_button(label="Download Resume 🔽", data=open("RESUME/John Feng Resume Hard Tech 2025-03-08.pdf",
                   "rb").read(), file_name="John Feng Resume Hard Tech 2025-03-08.pdf")
# Projects Section
st.markdown('<h2 class="section-title">📊 Projects  </h2>',
            unsafe_allow_html=True)

with st.expander("**Detector Frame-by-Frame Analysis Dashboard**", expanded=True):
    st.write("A dashboard that allows users to analyze detector data frame-by-frame")
    st.write("**Tech Stack:** " +
             ", ".join(['Python', 'Streamlit', 'Pandas', 'Plotly']))
    st.markdown(
        f"**Deployed App:** [{'https://frame-analyzer.streamlit.app/'}]({'https://frame-analyzer.streamlit.app/'})")
    st.caption(
        "*Note: This project is currently hosted on Streamlit Cloud, which may take a few seconds to load.")
    image_path = 'assets/frame-by-frame.gif'
    st.image(image_path)

with st.expander("**Pixel and Spectrum Analysis of Gamma-Ray Detector Data with Moving Mask**", expanded=True):
    st.write("This app allows users to analyze pixel and spectrum of gamma-ray detector data. The data is processed for each moving mask position to expose small areas of interest. The spectrum is calculated for each pixel and displayed in a spectrum plot.")
    st.write("**Tech Stack:** " +
             ", ".join(['Python', 'Streamlit', 'Pandas', 'Plotly']))
    st.markdown(
        f"**Deployed App:** [{'https://johnfeng-spectrum-analyzer.streamlit.app/'}]({'https://johnfeng-spectrum-analyzer.streamlit.app/'})")
    st.caption(
        "*Note: This project is currently hosted on Streamlit Cloud, which may take a few seconds to load.")
    image_path = 'assets/Spectrum-analyzer.gif'
    st.image(image_path)

with st.expander("**IV Curve Analysis of Semiconductor Devices**", expanded=True):
    st.write("A web app that allows users to analyze IV and Time-dependent Photocurrent curves of semiconductor devices.")
    st.write("**Tech Stack:** " +
             ", ".join(['Python', 'Streamlit', 'Pandas', 'Plotly', 'SciPy', 'NumPy']))
    st.markdown(
        "**Deployed App:** [https://mitacs-dashboard.streamlit.app/](https://mitacs-dashboard.streamlit.app/)")
    st.caption(
        "*Note: This project is currently hosted on Streamlit Cloud, which may take a few seconds to load.")
    image_path = 'assets/mitacs_dashboard.png'
    st.image(image_path, width=600)

with st.expander("**PrepPal - AI-Powered English Exam Prep**", expanded=True):
    st.write("Winner of 2023 Brave AI Accelerator Hackathon. A web app that uses AI to help users prepare for English proficiency exams such as IELTS and TOEFL. The app generates writing and reading practice questions and provides instant feedback.")
    st.write("**Tech Stack:** " +
             ", ".join(['Python', 'Streamlit', 'OpenAI', 'LangChain']))
    st.markdown(
        "**Pitch Deck:** [Google Slides](https://docs.google.com/presentation/d/1K5R1EqNaB_1PF3__VHCqVmuKlmQAU5qk7C30wgXWBjQ/edit?usp=sharing)  ")
    st.markdown(
        f"**Deployed App:** [{'https://preppal.streamlit.app/'}]({'https://preppal.streamlit.app/'})")
    st.caption(
        "*Note: This project is currently hosted on Streamlit Cloud, which may take a few seconds to load.")
    image_path = 'assets/hackathon_winners_cropped.jpeg'
    image = Image.open(image_path)
    st.image(image, width=400)

st.html("<hr class='solid'>")

# Contact Section
st.markdown('<h2 class="section-title">📬 Contact</h2>', unsafe_allow_html=True)
contact_col1, contact_col2 = st.columns(2)
with contact_col1:
    st.markdown("""
    ### Get in Touch
    - 📧 Email: johnfengphd@gmail.com
    - 📞 Phone: (647) 716 7981
    - 📍 Location: 
        * Toronto, ON, Canada
        * Victoria, BC, Canada
    """)

with contact_col2:
    st.markdown("""### Links""")
    # link_col1, link_col2 = st.columns(2)
    # with link_col1:
    #     image_path = 'assets/github_logo.png'
    #     st.image(image_path, width=20)
    # with link_col2:
    st.markdown("""
    - 💻 [GitHub](https://github.com/johnnykfeng)
    - 👨🏻‍💼 [LinkedIn](https://www.linkedin.com/in/john-feng-5735321b8/)
    """)

# Footer
st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #7f8c8d;">
        © 2025 John Feng. All rights reserved.
    </div>
""", unsafe_allow_html=True)
