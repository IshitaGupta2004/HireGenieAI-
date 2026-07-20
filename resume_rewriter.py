from llm import llm


class ResumeRewriter:

    ########################################################

    def rewrite(self, resume_text):

        rewritten_resume = llm.rewrite_resume(

            resume_text

        )

        return rewritten_resume

    ########################################################

    def save(self, rewritten_resume, output_file):

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                rewritten_resume

            )

        return output_file


rewriter = ResumeRewriter()
