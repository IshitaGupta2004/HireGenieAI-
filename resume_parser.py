import fitz
import pdfplumber
import docx
import re
import os

# ----------------------------
# Skills Database
# ----------------------------

SKILLS = [

    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",

    "html",
    "css",
    "bootstrap",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    "excel",
    "power bi",
    "tableau",

    "pandas",
    "numpy",

    "matplotlib",
    "seaborn",

    "machine learning",
    "deep learning",

    "tensorflow",
    "keras",
    "pytorch",

    "opencv",

    "nlp",

    "streamlit",
    "flask",
    "django",
    "fastapi",

    "git",
    "github",

    "docker",

    "linux",

    "aws",
    "azure"

]

# ----------------------------
# Resume Parser
# ----------------------------


class ResumeParser:

    ##########################################

    def read_pdf(self, path):

        text = ""

        with pdfplumber.open(path) as pdf:

            for page in pdf.pages:

                content = page.extract_text()

                if content:

                    text += content + "\n"

        return text

    ##########################################

    def read_docx(self, path):

        doc = docx.Document(path)

        text = ""

        for para in doc.paragraphs:

            text += para.text + "\n"

        return text

    ##########################################

    def extract_text(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":

            return self.read_pdf(file_path)

        if extension == ".docx":

            return self.read_docx(file_path)

        return ""

    ##########################################

    def extract_email(self, text):

        email = re.findall(

            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

            text

        )

        if email:

            return email[0]

        return ""

    ##########################################

    def extract_phone(self, text):

        phone = re.findall(

            r"(\+91[- ]?)?[6-9]\d{9}",

            text

        )

        if phone:

            return phone[0]

        return ""

    ##########################################

    def extract_name(self, text):

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if len(line.split()) >= 2:

                return line

        return ""

    ##########################################

    def extract_skills(self, text):

        found = []

        lower = text.lower()

        for skill in SKILLS:

            if skill in lower:

                found.append(skill.title())

        return sorted(list(set(found)))

    ##########################################

    def extract_education(self, text):

        education = []

        keywords = [

            "b.tech",

            "btech",

            "m.tech",

            "mtech",

            "b.e",

            "be",

            "bca",

            "mca",

            "b.sc",

            "m.sc",

            "phd"

        ]

        lower = text.lower()

        for key in keywords:

            if key in lower:

                education.append(key.upper())

        return education

    ##########################################

    def extract_experience(self, text):

        years = re.findall(

            r"(\d+)\+?\s*(year|years)",

            text.lower()

        )

        if years:

            return years[0][0] + " Years"

        return "Fresher"

    ##########################################

    def extract_projects(self, text):

        projects = []

        lines = text.split("\n")

        capture = False

        for line in lines:

            if "project" in line.lower():

                capture = True

                continue

            if capture:

                if line.strip() == "":

                    break

                projects.append(line.strip())

        return projects

    ##########################################

    def parse_resume(self, path):

        text = self.extract_text(path)

        data = {

            "name": self.extract_name(text),

            "email": self.extract_email(text),

            "phone": self.extract_phone(text),

            "skills": self.extract_skills(text),

            "education": self.extract_education(text),

            "experience": self.extract_experience(text),

            "projects": self.extract_projects(text),

            "text": text

        }

        return data


parser = ResumeParser()
