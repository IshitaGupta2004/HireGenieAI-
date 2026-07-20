from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME
from prompts import *

class HireGenieLLM:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

        self.model = MODEL_NAME

    ###########################################################

    def generate(self, prompt):

        try:

            response = self.client.chat.completions.create(

                model=self.model,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.3,

                max_tokens=2048

            )

            return response.choices[0].message.content

        except Exception as e:

            return f"Groq Error : {str(e)}"

    ###########################################################
    ## Resume Rewrite
    ###########################################################

    def rewrite_resume(self, resume_text):

        prompt = resume_rewrite_prompt(
            resume_text
        )

        return self.generate(prompt)

    ###########################################################
    ## ATS Explanation
    ###########################################################

    def explain_ats(

            self,

            resume,

            job,

            score,

            missing

    ):

        prompt = ats_explanation_prompt(

            resume,

            job,

            score,

            missing

        )

        return self.generate(prompt)

    ###########################################################
    ## Interview Questions
    ###########################################################

    def interview_questions(

            self,

            resume,

            job

    ):

        prompt = interview_prompt(

            resume,

            job

        )

        return self.generate(prompt)

    ###########################################################
    ## Career Roadmap
    ###########################################################

    def roadmap(

            self,

            skills,

            role

    ):

        prompt = roadmap_prompt(

            skills,

            role

        )

        return self.generate(prompt)

    ###########################################################
    ## Cover Letter
    ###########################################################

    def cover_letter(

            self,

            resume,

            company,

            role

    ):

        prompt = cover_letter_prompt(

            resume,

            company,

            role

        )

        return self.generate(prompt)

    ###########################################################
    ## Candidate Summary
    ###########################################################

    def candidate_summary(

            self,

            resume

    ):

        prompt = candidate_summary_prompt(

            resume

        )

        return self.generate(prompt)

    ###########################################################
    ## HR Recommendation
    ###########################################################

    def hr_recommendation(

            self,

            resume,

            job

    ):

        prompt = hr_recommendation_prompt(

            resume,

            job

        )

        return self.generate(prompt)

    ###########################################################
    ## Resume Chat
    ###########################################################

    def resume_chat(

            self,

            resume,

            question

    ):

        prompt = resume_chat_prompt(

            resume,

            question

        )

        return self.generate(prompt)

llm = HireGenieLLM()
