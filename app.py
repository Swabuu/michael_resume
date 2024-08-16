from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "michael.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Michael Mackie"
PAGE_ICON = ":wave:"
NAME = "Michael Mackie"
DESCRIPTION = """
Entrepreneur | Successful business owner
"""
EMAIL = "michael.mackie@proton.me"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
st.write("#")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qulifications")
st.write(
    """
✔️ 20 years of professional experience in the construction industry, with a focus on project and contract management  
✔️ Adept at building strong client relationships and delivering projects that exceed expectations   
✔️ Excellent problem-solving abilities, with a hands-on approach to overcoming challenges on-site
"""
)


# --- About ---

st.write("#")
st.subheader("About")
st.write(
    """
    #bygg #entreprenad #entrepreneur

Hi! I'm Michael! 

A motivated and proactive entrepreneur, I have a proven track record of building and leading successful ventures. As the Founder of Mike Alan Bygg och Entreprenad AB, I gained extensive experience in project and contract management, budget planning, and day-to-day construction operations, establishing a reputation for excellence in the construction industry. My hands-on approach and problem-solving skills have been pivotal in delivering high-quality projects. 
In addition to my construction expertise, I founded ConnectXpress AB and co-founded Mackie Mobile LLC, where I continue to apply my entrepreneurial spirit to innovate and lead in both telecommunications and secure communication solutions.
    """)


# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 0
st.write("🚧", "**Founder @ ConnectXpress AB** | Linköping, Sweden")
st.write("2024 - Present")
st.write(
    """
Your one-stop shop for telecommunications & fraud prevention - designed with security in mind, brought to you with connectivity in mind.

Founded in Sweden in 2024, ConnectXpress AB emerges as a leader in innovation in the telecommunications landscape. With over a decade of collective telecommunication experience, our team is dedicated to revolutionizing connectivity solutions. At ConnectXpress, we provide a range of services including A2P SMS messaging connectivity, virtual numbers, number lookup services, fraud prevention, and operator services.

🛡️ Protectify Networks  
🌐 Connectify Networks  
🔎 Verify Networks

Connect, Protect & Verify
Harnessing Machine Learning and Adaptive Technology to Secure Telecommunications.
"""
)

# --- JOB 0
st.write("🚧", "**Co-founder** @ Mackie Mobile LLC | Linköping, Sweden")
st.write("2024 - Present")
st.write(
    """
Communicate in privacy with the world's most secure phone plans.
"""
)

# --- JOB 1
st.write("🚧", "**Founder @ Mike Alan Bygg och Entreprenad AB** | Linköping, Sweden")
st.write("2021 - 2024")
st.write(
    """
- Project Management
- Contract Management
- Budget Planning
- Procurement
- Day-to-day construction work
"""
)
#- ► Responsible for EMEA 
# --- JOB 2
st.write("#")
st.write("🚧", "**Construction Worker @ CEFAB AB** | Linköping, Sweden")
st.write("2019 - 2021")
st.write(
    """
- Project Management
- Construction work
"""
)

# --- JOB 3
st.write("#")
st.write("🚧", "**Construction Worker @ Comfort AB** | Linköping, Sweden")
st.write("2017 - 2019")
st.write(
    """
- Project Management
- Construction work
"""
)
