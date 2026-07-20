from llm import llm


class HRDashboard:

    #######################################################

    def candidate_summary(

        self,

        resume_text

    ):

        return llm.candidate_summary(

            resume_text

        )

    #######################################################

    def hiring_recommendation(

        self,

        resume_text,

        job_description

    ):

        return llm.hr_recommendation(

            resume_text,

            job_description

        )


hr = HRDashboard()
