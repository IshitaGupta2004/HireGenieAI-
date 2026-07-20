############################################################
# Resume Rewrite Prompt
############################################################

def resume_rewrite_prompt(resume):

    return f"""
You are an expert ATS Resume Writer.

Rewrite the following resume professionally.

Rules:
- Improve grammar.
- Improve formatting.
- Keep facts unchanged.
- Add action verbs.
- Make it ATS friendly.
- Keep the resume concise.

Resume:

{resume}
"""


############################################################
# ATS Explanation Prompt
############################################################

def ats_explanation_prompt(

        resume,

        job,

        score,

        missing

):

    return f"""
You are an ATS Expert.

Resume ATS Score:
{score}/100

Missing Skills:
{missing}

Job Description:

{job}

Resume:

{resume}

Explain:

1. Why this ATS score was achieved.
2. Missing skills.
3. Resume strengths.
4. Resume weaknesses.
5. Improvements.
"""


############################################################
# Interview Questions Prompt
############################################################

def interview_prompt(

        resume,

        job

):

    return f"""
You are a Technical Interviewer.

Resume:

{resume}

Job Description:

{job}

Generate:

- 10 Technical Questions
- 5 HR Questions
- 5 Project Questions
- Expected Answers
- Difficulty Level
"""


############################################################
# Career Roadmap Prompt
############################################################

def roadmap_prompt(

        skills,

        role

):

    return f"""
Candidate Skills:

{skills}

Target Role:

{role}

Create a complete roadmap.

Include:

1. Skills to Learn
2. Courses
3. Projects
4. Certifications
5. Timeline
6. Interview Preparation
"""


############################################################
# Cover Letter Prompt
############################################################

def cover_letter_prompt(

        resume,

        company,

        role

):

    return f"""
Write a professional cover letter.

Company:

{company}

Role:

{role}

Candidate Resume:

{resume}

Keep it one page.
"""


############################################################
# Candidate Summary Prompt
############################################################

def candidate_summary_prompt(

        resume

):

    return f"""
Analyze this resume.

Generate:

- Candidate Summary
- Skills
- Experience
- Projects
- Strengths
- Weaknesses
- Overall Rating (10)
- Hiring Recommendation

Resume:

{resume}
"""


############################################################
# HR Recommendation Prompt
############################################################

def hr_recommendation_prompt(

        resume,

        job

):

    return f"""
You are an HR Manager.

Resume:

{resume}

Job Description:

{job}

Should the candidate be hired?

Provide:

- Match Percentage
- Pros
- Cons
- Risk Factors
- Final Decision

Respond as an HR Manager.
"""


############################################################
# Resume Chat Prompt
############################################################

def resume_chat_prompt(

        resume,

        question

):

    return f"""
Resume:

{resume}

Question:

{question}

Answer only using the information available in the resume.
If information is unavailable, clearly state that.
"""
