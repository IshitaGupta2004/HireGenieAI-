import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(
            "hiregenie.db",
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    ######################################################

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT,

            email TEXT UNIQUE,

            password TEXT,

            role TEXT

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS resumes(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_email TEXT,

            resume_name TEXT,

            ats_score REAL,

            semantic_score REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """)

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS reports(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_email TEXT,

            report TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

        """)

        self.connection.commit()

    ######################################################

    def register_user(

        self,

        username,

        email,

        password,

        role

    ):

        self.cursor.execute(

            """

            INSERT INTO users

            (

                username,

                email,

                password,

                role

            )

            VALUES

            (

                ?,

                ?,

                ?,

                ?

            )

            """,

            (

                username,

                email,

                password,

                role

            )

        )

        self.connection.commit()

    ######################################################

    def login(

        self,

        email,

        password

    ):

        self.cursor.execute(

            """

            SELECT *

            FROM users

            WHERE

            email=?

            AND password=?

            """,

            (

                email,

                password

            )

        )

        return self.cursor.fetchone()

    ######################################################

    def save_resume(

        self,

        email,

        resume_name,

        ats,

        semantic

    ):

        self.cursor.execute(

            """

            INSERT INTO resumes

            (

                user_email,

                resume_name,

                ats_score,

                semantic_score

            )

            VALUES

            (

                ?,

                ?,

                ?,

                ?

            )

            """,

            (

                email,

                resume_name,

                ats,

                semantic

            )

        )

        self.connection.commit()

    ######################################################

    def save_report(

        self,

        email,

        report

    ):

        self.cursor.execute(

            """

            INSERT INTO reports

            (

                user_email,

                report

            )

            VALUES

            (

                ?,

                ?

            )

            """,

            (

                email,

                str(report)

            )

        )

        self.connection.commit()

    ######################################################

    def get_reports(

        self,

        email

    ):

        self.cursor.execute(

            """

            SELECT *

            FROM reports

            WHERE

            user_email=?

            """,

            (

                email,

            )

        )

        return self.cursor.fetchall()

    ######################################################

    def get_resumes(

        self,

        email

    ):

        self.cursor.execute(

            """

            SELECT *

            FROM resumes

            WHERE

            user_email=?

            """,

            (

                email,

            )

        )

        return self.cursor.fetchall()
    def get_all_resumes(self):
        self.cursor.execute(
            """ SELECT * FROM resumes ORDER BY ats_score DESC,semantic_score DESC """
            )
        return self.cursor.fetchall()

    
    def get_all_reports(self):
        self.cursor.execute( """ SELECT * FROM reports ORDER BY created_at DESC """
                             )
        return self.cursor.fetchall()


db = Database()
