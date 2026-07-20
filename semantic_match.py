from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class SemanticMatcher:

    def __init__(self):

        print("Loading AI Embedding Model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Model Loaded Successfully!")

    ##########################################################

    def get_embedding(self, text):

        embedding = self.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding

    ##########################################################

    def similarity_score(

            self,

            resume_text,

            job_description

    ):

        resume_embedding = self.get_embedding(
            resume_text
        )

        job_embedding = self.get_embedding(
            job_description
        )

        similarity = cosine_similarity(

            [resume_embedding],

            [job_embedding]

        )[0][0]

        return round(float(similarity) * 100, 2)

    ##########################################################

    def rank_candidates(

            self,

            resumes,

            job_description

    ):

        ranking = []

        job_embedding = self.get_embedding(
            job_description
        )

        for candidate in resumes:

            embedding = self.get_embedding(

                candidate["text"]

            )

            score = cosine_similarity(

                [embedding],

                [job_embedding]

            )[0][0]

            ranking.append(

                {

                    "name": candidate["name"],

                    "score": round(float(score) * 100, 2)

                }

            )

        ranking = sorted(

            ranking,

            key=lambda x: x["score"],

            reverse=True

        )

        return ranking

    ##########################################################

    def confidence(self, score):

        if score >= 90:

            return "Excellent Match"

        elif score >= 80:

            return "Very Good Match"

        elif score >= 70:

            return "Good Match"

        elif score >= 60:

            return "Average Match"

        elif score >= 40:

            return "Weak Match"

        return "Poor Match"


matcher = SemanticMatcher()
