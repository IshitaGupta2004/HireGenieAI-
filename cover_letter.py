from llm import llm


class CoverLetterGenerator:

    ##########################################################

    def generate(

        self,

        resume,

        company,

        role

    ):

        return llm.cover_letter(

            resume,

            company,

            role

        )

    ##########################################################

    def save(

        self,

        letter,

        output_file

    ):

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                letter

            )

        return output_file


cover = CoverLetterGenerator()
