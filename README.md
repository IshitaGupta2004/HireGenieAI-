#  HireGenie AI

### AI-Powered ATS Resume Screening & Recruitment Assistant

HireGenie AI is an AI-powered recruitment platform designed to help **job applicants improve their resumes** and help **HR professionals screen and evaluate candidates** more efficiently.

The system analyzes a candidate's resume against a given job description, calculates an ATS score, identifies matched and missing skills, and provides personalized recommendations. It also uses AI to generate resume improvements, interview questions, cover letters, career roadmaps, candidate summaries, and hiring recommendations.

---

##  Project Overview

Recruitment companies and HR departments often receive a large number of resumes for a single job position. Manually checking every resume takes considerable time and effort.

At the same time, applicants often do not know:

* Whether their resume is ATS-friendly
* Which skills are missing
* Why their resume may not be shortlisted
* How to improve their resume
* What questions they may face in an interview
* How to write a professional cover letter

**HireGenie AI** addresses these problems by bringing resume analysis, ATS screening, and AI-powered career assistance into a single application.

---

##  Objectives

The main objectives of HireGenie AI are:

* Automate resume screening.
* Calculate an ATS compatibility score.
* Compare resumes with job descriptions.
* Identify matched and missing skills.
* Perform semantic similarity analysis.
* Provide personalized resume improvement suggestions.
* Rewrite resumes using AI.
* Generate job-specific interview questions.
* Generate personalized cover letters.
* Create career roadmaps.
* Provide an AI-powered resume chat assistant.
* Help HR professionals rank candidates.
* Generate candidate summaries.
* Provide AI-based hiring recommendations.

---

#  How the System Works

The basic workflow of the application is:

```text
User
  ↓
Login / Registration
  ↓
Upload Resume
  ↓
Enter Job Description
  ↓
Resume Parsing
  ↓
Extract Resume Information
  ↓
ATS Analysis
  ↓
Skill Matching
  ↓
Semantic Similarity
  ↓
ATS Score + Analysis
  ↓
AI-Powered Features
  ├── Resume Rewrite
  ├── Interview Questions
  ├── Cover Letter
  ├── Career Roadmap
  └── Resume Chat
  ↓
Store Results
  ↓
HR Dashboard
  ↓
Candidate Ranking & Recommendation
```

---

#  Main Modules

## 1. Authentication Module

The authentication module manages user registration and login.

It allows different users to access the appropriate part of the application.

### Functions

* User registration
* User login
* Session management
* Applicant access
* HR access

---

## 2. Resume Upload Module

Applicants can upload their resumes to the system.

The application supports common resume formats such as:

* PDF
* DOCX

The uploaded resume is then passed to the resume parser.

---

## 3. Resume Parser

The Resume Parser extracts readable text and important information from the uploaded resume.

It can identify information such as:

* Education
* Technical skills
* Projects
* Experience
* Certifications
* Achievements

The extracted information becomes the input for further analysis.

---

## 4. ATS Scoring Module

The ATS module compares the resume with the provided job description.

The system checks relevant information such as:

* Required skills
* Keywords
* Education
* Experience
* Resume content

The result is converted into an ATS score that indicates how closely the resume matches the job requirements.

---

## 5. Semantic Matching

Keyword matching alone may not always understand the meaning of a resume.

Therefore, HireGenie AI also performs semantic similarity analysis.

The system uses techniques such as:

**TF-IDF Vectorization + Cosine Similarity**

to convert text into numerical representations and calculate how similar the resume is to the job description.

A higher similarity indicates that the resume content is more closely related to the job requirements.

---

## 6. Missing Skill Detection

After comparing the resume with the job description, the system identifies:

### Matched Skills

Skills that are present in both the resume and job requirements.

### Missing Skills

Important skills mentioned in the job description but not found in the resume.

This helps applicants understand what they need to improve.

---

#  AI Features

HireGenie AI provides several AI-powered features.

### Resume Rewriter

The system analyzes the existing resume and generates an improved version with better wording, structure, and job-related keywords.

### Interview Question Generator

The system generates interview questions based on the candidate's resume and target job.

### Cover Letter Generator

It creates a personalized cover letter based on:

* Resume
* Company
* Job role

### Career Roadmap

The system suggests a learning and career roadmap based on the candidate's current skills and target role.

### Resume Chat

Applicants can ask questions about their resume and receive AI-generated responses.

### Candidate Summary

The HR module can generate a concise summary of a candidate's profile.

### Hiring Recommendation

The system provides an AI-assisted recommendation based on the candidate's resume and job requirements.

---

#  HR Dashboard

The HR module is designed to simplify candidate evaluation.

HR professionals can:

* View candidates
* View candidate resumes
* Check ATS scores
* Compare candidates
* Rank applicants
* Generate candidate summaries
* Get AI-based hiring recommendations

This reduces the amount of manual resume screening required.

---

#  Database

HireGenie AI uses **SQLite** for storing application data.

The database can store information such as:

```text
Users
Candidates
Resumes
Job Descriptions
ATS Scores
Skills
Analysis Results
AI Generated Results
```

SQLite was selected because it is lightweight, simple to configure, and suitable for a project of this scale.

---

#  System Architecture

```
                   ┌──────────────────┐
                   │      User        │
                   └────────┬─────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Streamlit      │
                 │     Frontend        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Application Logic │
                 └──────────┬──────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
   Resume Parser       ATS Engine       AI Engine
          │                 │                 │
          │                 ▼                 ▼
          │          Semantic Matching    LLM/Ollama
          │
          └─────────────────┬─────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    SQLite     │
                    │   Database    │
                    └───────────────┘
```

---

#  Technologies Used

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Main programming language |
| Streamlit           | Web application interface |
| SQLite              | Database                  |
| Pandas              | Data processing           |
| Scikit-learn        | Semantic matching         |
| TF-IDF              | Text vectorization        |
| Cosine Similarity   | Similarity calculation    |
| PyPDF2 / PDF Parser | PDF resume extraction     |
| python-docx         | DOCX processing           |
| Ollama / LLM        | AI-generated responses    |
| GitHub              | Source code management    |

---

#  Project Structure

A typical project structure is:

```text
HireGenie-AI/
│
├── app.py
├── llm.py
├── config.py
├── prompts.py
├── database.py
├── ats_engine.py
├── resume_parser.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── applicant.py
│   ├── hr_dashboard.py
│   ├── resume_analysis.py
│   └── ai_tools.py
│
├── models/
│   └── ...
│
├── utils/
│   └── ...
│
└── data/
    └── ...
```

The exact files may differ depending on the final version of the project.

---

#  ATS Analysis Example

Suppose the job description contains:

```text
Python
Machine Learning
SQL
TensorFlow
Streamlit
Git
```

and the candidate's resume contains:

```text
Python
Machine Learning
SQL
Pandas
Streamlit
```

The system can identify:

### Matched Skills

```text
Python
Machine Learning
SQL
Streamlit
```

### Missing Skills

```text
TensorFlow
Git
```

The applicant can then improve the resume by adding relevant skills they genuinely possess.

---

#  Advantages

* Saves HR screening time.
* Helps applicants improve resumes.
* Provides automated ATS analysis.
* Identifies missing skills.
* Provides personalized AI assistance.
* Supports interview preparation.
* Generates professional cover letters.
* Helps HR rank candidates.
* Provides a centralized recruitment platform.
* Easy-to-use web interface.

---

#  Limitations

* ATS results depend on the quality of the resume and job description.
* Resume parsing may not work perfectly with highly complex layouts.
* AI-generated content should be reviewed by the user.
* Semantic similarity does not guarantee actual job suitability.
* Local LLM usage through Ollama requires the model to be installed and running.
* The current system is primarily designed as a project prototype.

---

#  Future Scope

The project can be improved further by adding:

* Cloud deployment
* Multi-language resume analysis
* Voice-based interview preparation
* Video interview analysis
* LinkedIn integration
* Email notifications
* Advanced HR analytics
* Company-specific ATS scoring
* Multiple LLM support
* Cloud database
* Resume template generation
* Automated job recommendations
* Real-time recruitment analytics

---

#  Testing

The system can be tested using different resumes and job descriptions.

### Test Cases

| Test                | Input               | Expected Result           |
| ------------------- | ------------------- | ------------------------- |
| Login               | Valid credentials   | Dashboard opens           |
| Registration        | New user details    | Account created           |
| Resume Upload       | PDF resume          | Resume accepted           |
| Resume Upload       | DOCX resume         | Resume accepted           |
| ATS Analysis        | Resume + JD         | ATS score generated       |
| Skill Matching      | Resume + JD         | Matched skills displayed  |
| Missing Skills      | Resume + JD         | Missing skills displayed  |
| Resume Rewrite      | Resume              | Improved resume generated |
| Interview Questions | Resume + JD         | Questions generated       |
| Cover Letter        | Resume + Role       | Cover letter generated    |
| Career Roadmap      | Skills + Role       | Roadmap generated         |
| HR Ranking          | Multiple candidates | Candidates ranked         |

---

# Expected Results

After successful implementation, HireGenie AI provides:

```text
Resume
   ↓
Resume Analysis
   ↓
ATS Score
   ↓
Matched Skills
   ↓
Missing Skills
   ↓
Improvement Suggestions
   ↓
AI Assistance
```

For HR:

```text
Candidates
   ↓
Resume Analysis
   ↓
ATS Scores
   ↓
Candidate Ranking
   ↓
AI Candidate Summary
   ↓
Hiring Recommendation
```

---

#  Learning Outcomes

Through the development of this project, the following skills were gained:

* Python programming
* AI integration
* Machine Learning
* Natural Language Processing
* Prompt Engineering
* Large Language Models
* Resume parsing
* Text processing
* Semantic similarity
* Database management
* Streamlit development
* API/LLM integration
* Debugging
* Software testing
* GitHub project management

---

#  Conclusion

HireGenie AI demonstrates how Artificial Intelligence can be applied to solve practical problems in the recruitment process.

The system provides a single platform where applicants can analyze and improve their resumes, prepare for interviews, generate cover letters, and receive career guidance. At the same time, HR professionals can analyze candidates, compare resumes, rank applicants, and receive AI-assisted hiring recommendations.

By combining **ATS analysis, semantic matching, resume parsing, SQLite database management, Streamlit, and AI/LLM technology**, HireGenie AI provides an efficient and user-friendly recruitment assistance solution.

The project also provides a strong foundation for future development into a larger cloud-based recruitment platform.

---

##  Project Type

**Academic / Internship Project**

### Domain

**Artificial Intelligence | Machine Learning | NLP | Recruitment Technology**

### Primary Users

* Job Applicants
* HR Professionals
* Recruiters

---

##  License

This project is developed for educational and project demonstration purposes.

---

## ⭐ If you find this project useful

Give the repository a ⭐ on GitHub.
