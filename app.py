import os
import streamlit as st

from auth import auth
from database import db

from resume_parser import parser
from ats_engine import ats
from semantic_match import matcher

from resume_rewriter import rewriter
from interview_generator import generator
from cover_letter import cover
from career_roadmap import roadmap

from llm import llm
from hr_dashboard import hr

#########################################################
# Streamlit Configuration
#########################################################

st.set_page_config(
    page_title="HireGenie AI",
    
    layout="wide",
    initial_sidebar_state="expanded"
)

#########################################################
# Session State
#########################################################

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "resume" not in st.session_state:
    st.session_state.resume = None

if "report" not in st.session_state:
    st.session_state.report = None

if "job" not in st.session_state:
    st.session_state.job = ""

#########################################################
# Sidebar
#########################################################

st.sidebar.title("HireGenie AI")
st.sidebar.markdown("---")

if st.session_state.logged_in:

    st.sidebar.success(
        f"Welcome {st.session_state.user['username']}"
    )

    st.sidebar.write(
        f"Role : {st.session_state.user['role']}"
    )

    st.sidebar.markdown("---")

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.resume = None
        st.session_state.report = None
        st.session_state.job = ""

        st.rerun()

#########################################################
# Main Title
#########################################################

st.title("HireGenie AI")
st.caption("AI Powered ATS Resume Screening System by Ishita Gupta")
st.markdown("---")

#########################################################
# Login / Register
#########################################################

if not st.session_state.logged_in:

    menu = st.sidebar.radio(
        "Menu",
        ["Login", "Register"]
    )

    #####################################################
    # Register
    #####################################################

    if menu == "Register":

        st.subheader("Create Account")

        username = st.text_input(
            "Username",
            key="reg_username"
        )

        email = st.text_input(
            "Email",
            key="reg_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="reg_password"
        )

        confirm = st.text_input(
            "Confirm Password",
            type="password",
            key="reg_confirm"
        )

        role = st.selectbox(
            "Role",
            ["Applicant", "HR"],
            key="reg_role"
        )

        if st.button(
            "Register",
            key="register_button"
        ):

            if username == "" or email == "" or password == "":
                st.error("Please fill all fields.")

            elif password != confirm:
                st.error("Passwords do not match.")

            else:

                success = auth.register(
                    username,
                    email,
                    password,
                    role
                )

                if success:
                    st.success("Registration Successful")
                    st.info("Please Login")

                else:
                    st.error("User already exists")

    #####################################################
    # Login
    #####################################################

    else:

        st.subheader("Login")

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login",
            key="login_button"
        ):

            user = auth.login(
                email,
                password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.user = user

                st.rerun()

            else:

                st.error("Invalid Email or Password")


#########################################################
# Applicant Dashboard
#########################################################

if st.session_state.logged_in and st.session_state.user["role"] == "Applicant":

    st.header("Applicant Dashboard")

    #####################################################
    # Upload Resume
    #####################################################

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"],
        key="resume_upload"
    )

    job_description = st.text_area(
        "Paste Job Description",
        height=250,
        key="job_description"
    )

    #####################################################
    # Save Uploaded Resume
    #####################################################

    file_path = None

    if uploaded_file is not None:

        if not os.path.exists("resumes"):
            os.makedirs("resumes")

        file_path = os.path.join(
            "resumes",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("Resume Uploaded Successfully")

    #####################################################
    # Analyze Resume
    #####################################################

    if st.button(
        "Analyze Resume",
        key="analyze_resume"
    ):

        if uploaded_file is None:

            st.warning("Please upload a resume.")

        elif job_description.strip() == "":

            st.warning("Please paste the Job Description.")

        else:

            with st.spinner("Analyzing Resume..."):

                resume = parser.parse_resume(file_path)

                report = ats.analyze(
                    resume,
                    job_description
                )

                semantic = matcher.similarity_score(
                    resume["text"],
                    job_description
                )

                db.save_resume(
                    st.session_state.user["email"],
                    uploaded_file.name,
                    report["ATS Score"],
                    semantic
                )

                db.save_report(
                    st.session_state.user["email"],
                    report
                )

                #################################################

                st.session_state.resume = resume
                st.session_state.report = report
                st.session_state.job = job_description
                st.session_state.semantic = semantic

            st.success("Analysis Completed Successfully")

    #####################################################
    # Display Report
    #####################################################

    if st.session_state.report is not None:

        report = st.session_state.report
        semantic = st.session_state.semantic

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "ATS Score",
                f"{report['ATS Score']}%"
            )

        with col2:

            st.metric(
                "Semantic Score",
                f"{semantic}%"
            )

        with col3:

            st.metric(
                "Matched Skills",
                len(report["Matched Skills"])
            )

        #################################################

        st.markdown("---")

        left, right = st.columns(2)

        with left:

            st.subheader("✅ Matched Skills")

            if report["Matched Skills"]:

                for skill in report["Matched Skills"]:
                    st.success(skill)

            else:

                st.warning("No matched skills found.")

        with right:

            st.subheader("❌ Missing Skills")

            if report["Missing Skills"]:

                for skill in report["Missing Skills"]:
                    st.error(skill)

            else:

                st.success("No missing skills.")

        #################################################

        st.subheader("Suggestions")

        if report["Suggestions"]:

            for suggestion in report["Suggestions"]:
                st.info(suggestion)

        else:

            st.success("Excellent Resume!")

#########################################################
# AI Career Assistant
#########################################################

if st.session_state.resume is not None:

    st.markdown("---")
    st.header("AI Career Assistant")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Resume Rewriter",
            "Interview Questions",
            "Cover Letter",
            "Career Roadmap"
        ]
    )

    #################################################
    # Resume Rewriter
    #################################################

    with tab1:

        st.subheader("ATS Resume Rewriter")

        if st.button(
            "Rewrite Resume",
            key="rewrite_resume_btn"
        ):

            with st.spinner("Rewriting Resume..."):

                st.session_state.rewritten_resume = rewriter.rewrite(
                    st.session_state.resume["text"]
                )

        if "rewritten_resume" in st.session_state:

            st.text_area(
                "Improved Resume",
                value=st.session_state.rewritten_resume,
                height=450,
                key="rewrite_output"
            )

    #################################################
    # Interview Questions
    #################################################

    with tab2:

        st.subheader("Interview Questions")

        if st.button(
            "Generate Interview Questions",
            key="interview_btn"
        ):

            with st.spinner("Generating Questions..."):

                st.session_state.interview_questions = generator.generate(
                    st.session_state.resume["text"],
                    st.session_state.job
                )

        if "interview_questions" in st.session_state:

            st.text_area(
                "Interview Questions",
                value=st.session_state.interview_questions,
                height=450,
                key="interview_output"
            )

    #################################################
    # Cover Letter
    #################################################

    with tab3:

        st.subheader("Cover Letter Generator")

        company = st.text_input(
            "Company Name",
            key="company_input"
        )

        role = st.text_input(
            "Job Role",
            key="cover_role"
        )

        if st.button(
            "Generate Cover Letter",
            key="cover_btn"
        ):

            with st.spinner("Generating Cover Letter..."):

                st.session_state.cover_letter = cover.generate(
                    st.session_state.resume["text"],
                    company,
                    role
                )

        if "cover_letter" in st.session_state:

            st.text_area(
                "Generated Cover Letter",
                value=st.session_state.cover_letter,
                height=450,
                key="cover_output"
            )

    #################################################
    # Career Roadmap
    #################################################

    with tab4:

        st.subheader("Career Roadmap")

        target_role = st.text_input(
            "Target Role",
            key="roadmap_target_role"
        )

        if st.button(
            "Generate Roadmap",
            key="roadmap_btn"
        ):

            with st.spinner("Generating Roadmap..."):

                skills = ", ".join(
                    st.session_state.resume["skills"]
                )

                st.session_state.roadmap = roadmap.generate(
                    skills,
                    target_role
                )

        if "roadmap" in st.session_state:

            st.text_area(
                "Career Roadmap",
                value=st.session_state.roadmap,
                height=450,
                key="roadmap_output"
            )

#########################################################
# Resume Chat
#########################################################

if st.session_state.resume is not None:

    st.markdown("---")

    st.header("Ask About Your Resume")

    question = st.text_input(

        "Ask anything about your resume",

        key="resume_chat_question"

    )

    if st.button(

        "Ask AI",

        key="resume_chat_button"

    ):

        if question.strip() == "":

            st.warning(

                "Please enter your question."

            )

        else:

            with st.spinner(

                "Thinking..."

            ):

                st.session_state.chat_answer = llm.resume_chat(

                    st.session_state.resume["text"],

                    question

                )

    if "chat_answer" in st.session_state:

        st.success("Answer")

        st.write(

            st.session_state.chat_answer

        )

#########################################################
# Download Reports
#########################################################

if st.session_state.report is not None:

    st.markdown("---")

    st.header("Download Reports")

    st.download_button(

        label="Download ATS Report",

        data=str(

            st.session_state.report

        ),

        file_name="ATS_Report.txt",

        mime="text/plain",

        key="download_report"

    )

    st.download_button(

        label="Download Parsed Resume",

        data=st.session_state.resume["text"],

        file_name="Parsed_Resume.txt",

        mime="text/plain",

        key="download_resume"

    )

#########################################################
# Resume History
#########################################################

st.markdown("---")

st.header("📁 Previous Resume Analysis")

history = db.get_resumes(

    st.session_state.user["email"]

)

if len(history) == 0:

    st.info(

        "No previous reports found."

    )

else:

    import pandas as pd

    history_df = pd.DataFrame(

        history,

        columns=[

            "ID",

            "Email",

            "Resume",

            "ATS Score",

            "Semantic Score",

            "Date"

        ]

    )

    st.dataframe(

        history_df,

        use_container_width=True

    )


#########################################################
# HR Dashboard
#########################################################

if st.session_state.logged_in and st.session_state.user["role"] == "HR":

    st.header("💼 HR Dashboard")

    resumes = db.get_all_resumes()

    if len(resumes) == 0:

        st.info("No resumes found.")

    else:

        import pandas as pd

        columns = [
            "ID",
            "Email",
            "Resume",
            "ATS Score",
            "Semantic Score",
            "Date"
        ]

        df = pd.DataFrame(
            resumes,
            columns=columns
        )

        st.subheader("Candidate Database")

        st.dataframe(
            df,
            use_container_width=True
        )

        #################################################

        st.markdown("---")

        st.subheader("Candidate Ranking")

        ranking = df.sort_values(
            by=[
                "ATS Score",
                "Semantic Score"
            ],
            ascending=False
        )

        st.dataframe(
            ranking,
            use_container_width=True
        )

        #################################################

        st.markdown("---")

        st.subheader("Top Candidate")

        top = ranking.iloc[0]

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "ATS Score",
                top["ATS Score"]
            )

        with col2:

            st.metric(
                "Semantic Score",
                top["Semantic Score"]
            )

        st.success(
            f"""
Best Candidate

Email : {top['Email']}

Resume : {top['Resume']}
"""
        )

        #################################################

        st.markdown("---")

        st.subheader("Candidate Analytics")

        st.bar_chart(
            ranking.set_index("Resume")[
                [
                    "ATS Score",
                    "Semantic Score"
                ]
            ]
        )

        #################################################

        st.subheader("Score Distribution")

        st.line_chart(
            ranking[
                [
                    "ATS Score",
                    "Semantic Score"
                ]
            ]
        )

        #################################################

        st.markdown("---")

        st.subheader("Select Candidate")

        selected_resume = st.selectbox(
            "Choose Resume",
            ranking["Resume"].tolist(),
            key="candidate_selector"
        )

        selected = ranking[
            ranking["Resume"] == selected_resume
        ].iloc[0]

        st.write(selected)    
            
