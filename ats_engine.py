import re


class ATSEngine:

    def __init__(self):

        self.skill_weight = 40
        self.experience_weight = 20
        self.education_weight = 15
        self.resume_weight = 15
        self.keyword_weight = 10

    ########################################################

    def clean_text(self, text):

        text = text.lower()

        text = re.sub(r'[^a-z0-9 ]', ' ', text)

        return text

    ########################################################

    def extract_keywords(self, text):

        text = self.clean_text(text)

        words = text.split()

        words = list(set(words))

        return words

    ########################################################

    def skill_score(self, resume_skills, job_description):

        job_keywords = self.extract_keywords(job_description)

        matched = []

        for skill in resume_skills:

            if skill.lower() in job_keywords:

                matched.append(skill)

        if len(job_keywords) == 0:

            return 0, matched

        score = (

            len(matched)

            /

            len(job_keywords)

        ) * self.skill_weight

        score = min(score, self.skill_weight)

        return round(score, 2), matched

    ########################################################

    def keyword_score(self, resume_text, job_description):

        resume = self.clean_text(resume_text)

        keywords = self.extract_keywords(job_description)

        count = 0

        for word in keywords:

            if word in resume:

                count += 1

        score = (

            count

            /

            len(keywords)

        ) * self.keyword_weight

        return round(min(score, self.keyword_weight), 2)

    ########################################################

    def experience_score(self, experience):

        if experience == "Fresher":

            return 10

        years = re.findall(r"\d+", experience)

        if not years:

            return 10

        years = int(years[0])

        if years >= 5:

            return 20

        elif years >= 3:

            return 18

        elif years >= 2:

            return 16

        elif years >= 1:

            return 14

        return 10

    ########################################################

    def education_score(self, education):

        if len(education) == 0:

            return 0

        return self.education_weight

    ########################################################

    def resume_quality(self, resume):

        score = 0

        if resume["name"]:

            score += 2

        if resume["email"]:

            score += 2

        if resume["phone"]:

            score += 2

        if resume["skills"]:

            score += 3

        if resume["education"]:

            score += 2

        if resume["projects"]:

            score += 2

        if resume["experience"]:

            score += 2

        return score

    ########################################################

    def missing_skills(self, resume_skills, job_description):

        keywords = self.extract_keywords(job_description)

        missing = []

        resume_lower = [

            skill.lower()

            for skill in resume_skills

        ]

        for word in keywords:

            if word not in resume_lower:

                if len(word) > 2:

                    missing.append(word)

        return sorted(list(set(missing)))

    ########################################################

    def suggestions(self, report):

        tips = []

        if report["Skill Score"] < 25:

            tips.append(

                "Add more technical skills related to the job."

            )

        if report["Experience Score"] < 15:

            tips.append(

                "Include internships or projects to strengthen experience."

            )

        if report["Resume Quality"] < 12:

            tips.append(

                "Complete all important resume sections."

            )

        if len(report["Missing Skills"]) > 5:

            tips.append(

                "Learn and include missing technologies."

            )

        if report["ATS Score"] < 70:

            tips.append(

                "Tailor your resume for each job description."

            )

        return tips

    ########################################################

    def analyze(

        self,

        resume,

        job_description

    ):

        skill_score, matched = self.skill_score(

            resume["skills"],

            job_description

        )

        keyword_score = self.keyword_score(

            resume["text"],

            job_description

        )

        experience_score = self.experience_score(

            resume["experience"]

        )

        education_score = self.education_score(

            resume["education"]

        )

        quality = self.resume_quality(

            resume

        )

        total = (

            skill_score

            + keyword_score

            + experience_score

            + education_score

            + quality

        )

        total = round(min(total, 100), 2)

        report = {

            "ATS Score": total,

            "Skill Score": skill_score,

            "Keyword Score": keyword_score,

            "Experience Score": experience_score,

            "Education Score": education_score,

            "Resume Quality": quality,

            "Matched Skills": matched,

            "Missing Skills": self.missing_skills(

                resume["skills"],

                job_description

            )

        }

        report["Suggestions"] = self.suggestions(

            report

        )

        return report


ats = ATSEngine()
