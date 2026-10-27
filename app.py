import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(
    page_title="John Prince Alonte | Portfolio",
    page_icon="👋",
    layout="wide",
)
st.title("John Prince Alonte | Portfolio")
with st.sidebar:
    st.header("Feedback Form")
    form = st.form("Feedback Form")
    with form:
        job = st.text_input("Job Title*")
        rating = st.slider(label="Rating*", value=5, min_value=0, max_value=10)
        best_section = st.selectbox("Best Section*", ["About me", "Autobiography", "Skills", "Projects"])
        needs_improvement = st.multiselect("Which sections need improvement*", ["About me", "Autobiography", "Skills", "Projects"])
        hirability = st.radio("If you were an employer, would you hire me?*", ["Yes", "No"])
        comment = st.text_area("Comments*")
        consent = st.checkbox("I understand that my data is kept anonymous and therefore is subject to data analytics.*")
        submitted = st.form_submit_button("Submit")
    if submitted:
        errors = []
        if not job.strip():
            errors.append("Jobs must not be empty")
        if not best_section.strip():
            errors.append("Best Section must not be empty")
        if not needs_improvement:
            errors.append("Needs Improvement must not be empty")
        if not comment.strip():
            errors.append("Comment must not be empty")
        if not consent:
            errors.append("Please give consent before submitting")
        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success(f"Thank you, your feedback is appreciated!")
about_me_tab, autobiography_tab, skills_tab, projects_tab = st.tabs(["About Me", "Autobiography", "Skills", "Projects"])
with about_me_tab:
    st.header("About me")
    about_me = {"Name": ["John Prince L. Alonte"], "Program":["Computer Science"], "Year":["3"], "Section":["F2"]}
    st.table(pd.DataFrame.from_dict(about_me, orient="index"), hide_header=True)
    image_col, biography_col = st.columns(2)
    with image_col:
        st.image("images/alonte_uniform.jpg")
    with biography_col:
        st.header("Short Biography")
        biography="John Prince Alonte is one of the most handsome guys to ever set foot in this planet." \
        " Anyone who has been blessed by a glimpse of this beauty has been starstruck and never again able to function normally. " \
        "This then resulted to the public fear of Prince's charms, which lead him to isolation. May he discover flaws and imperfections so that he will finally be " \
        "a normal human being."
        st.write(biography)
with autobiography_tab:
    st.header("Autobiography")
    autobiography = "As you may have already guessed, I'm **John Prince Alonte**, " \
    "a **Computer Science** student studying in **Cebu Institute of Technology - University**." \
    " I come from a humble background, with two younger full-blooded siblings and 3 half-blooded siblings." \
    " I studied at **Pardo Elementary Shool**, an elementary school from Pardo, if that isn't obvious enough," \
    " under the **Special Science Class** section, and I believe I was the **Salutatorian** (?)," \
    " which I don't how that happened as I don't remember working that hard." \
    "\n\nBefore the graduation though, I took an examination which I also don't know why I took and then" \
    " got admitted to **Philippine Science High School**, Pisay for short, a very humble high school in a" \
    " mountainous neighborhood in Argao.\n\nI'm particularly interested in hardware, so my first choice for my program" \
    " was Electronics Engineering, but unfortunately, as I immersed here in CIT-U under the dean of the College of Computer Studies," \
    " she told me that Electronics Engineering in CIT-U was bad, so I decided to go with Computer Science instead.\n\n" \
    "I then took the **University of the Philippines College Admission Test (UPCAT)** and **DOST Admission Exam** because it was mandatory in our school." \
    " For absolutely no apparent reason, I passed both, so obviously one would think that I would go to UP and enjoy my life with DOST money, but to my regret," \
    " I got sold by a certain dean that CIT-U was the best university for Computer Science.\n\nAfter taking those exams, my mom told me to take a scholarship" \
    " for whatever reason which I also passed for whatever reason and now I used that scholarship instead of DOST to take Computer Science in CIT-U because I don't like being bound by a contract" \
    " like I was bound in high school which forced me to choose a science program.\n\n" \
    "There was a time that I was able to reach **Top 1 status among all first years in CIT-U of all courses**, which is still one my most treasured achievements," \
    " which unfortunately did not last since long as I realized everyone was just cheating and using AI so what's the point. Thankfully though," \
    " I did not hop on this trend but the FOMO though."
    st.markdown(autobiography)
with skills_tab:
    st.header("Skills")
    skills = pd.DataFrame({"Skills":["Software Engineering", "Algorithmic Problem-Solving", "Mathematics", "Physics", "Embedded Systems", "Electronics"], "Percentage":[15, 30, 15, 25, 10, 5]})
    pie_chart = px.pie(skills, names="Skills", values="Percentage", title="Skills")
    st.plotly_chart(pie_chart)
    skills_dict = {
        "Skills": ["Algorithmic Problem-Solving",
                   "Physics",
                   "Mahematics",
                   "Embedded Systems",
                   "Electronics"],
        "Description": ["Optimization techniques learned from 560+ leetcode problems",
                        "Specialized in Physics in Philippine Science High School\n\n"
                        "Currently reading University Physics by Hugh D. Young, Roger A. Freedman, Francis W. Sears, and Mark W. Zemansky",
                        "Byproduct of Physics and Computer Science mathematical and theoretical natures. Further refined by leetcode mathematical optimizations",
                        "Slight knowledge around Raspberry Pi Pico handling and basic sensors",
                        "Miniscule skills in circuitry with and without microcontrollers"]
    }
    st.table(pd.DataFrame(skills_dict))
with projects_tab:
    st.header("Projects")
    projects = {
        "Project":["T(N) Analyzer",
                   "QR-Mapping Blind Navigation",
                   "Sabungero Idle Game"],
        "Role/s": ["Lead Developer, Co-Ideator",
                   "Lead Developer, Ideator",
                   "Lead Developer, Project Manager, Ideator"],
        "Tools":["JavaFX",
                 "Python, Android sensors and camera, YOLO (Object Detection), OpenCV (QR), Text to Speech, Speech to Text",
                 "Javascript, HTML, CSS"],
        "Output":["Uses drag and drop concept of the popular Scratch Programming Language "
        "to make a function and calculates the exact runtime representation for Data Analysis of Algorithms.\n\n"
        "Note: Backend logic was coded from scratch",
        "Uses phone magnetometer and accelerometer to record path taken for initial map generation. "
        "Uses TTS and STT to know which checkpoint the user wants to go and then uses shortest path algorithms to find the optimal path. "
        "Checkpoints are represented as QR codes that the camera can detect until the user reaches the target location. "
        "Object detection is used sparingly for path obstruction detection.\n\n"
        "Note: Entirely coded from scratch",
        "A javascript game made entirely in vanilla javascript: Play the game here: https://github.com/Hypothalamus143/Sabungero-Idle-Game"]
    }
    st.table(pd.DataFrame(projects))
