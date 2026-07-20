from llm import llm


class CareerRoadmap:

    ##########################################################

    def generate(

        self,

        skills,

        target_role

    ):

        roadmap = llm.roadmap(

            skills,

            target_role

        )

        return roadmap

    ##########################################################

    def save(

        self,

        roadmap,

        output_file

    ):

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                roadmap

            )

        return output_file


roadmap = CareerRoadmap()
