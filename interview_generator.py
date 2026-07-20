from llm import llm


class InterviewGenerator:

    ##########################################################

    def generate(

        self,

        resume,

        job_description

    ):

        return llm.interview_questions(

            resume,

            job_description

        )

    ##########################################################

    def save(

        self,

        questions,

        output_file

    ):

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                questions

            )

        return output_file


generator = InterviewGenerator()
