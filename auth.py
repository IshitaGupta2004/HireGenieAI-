import bcrypt

from database import db


class Authentication:

    ########################################################

    def hash_password(self, password):

        password = password.encode("utf-8")

        hashed = bcrypt.hashpw(

            password,

            bcrypt.gensalt()

        )

        return hashed.decode("utf-8")

    ########################################################

    def verify_password(

        self,

        password,

        hashed

    ):

        return bcrypt.checkpw(

            password.encode("utf-8"),

            hashed.encode("utf-8")

        )

    ########################################################

    def register(

        self,

        username,

        email,

        password,

        role

    ):

        hashed_password = self.hash_password(

            password

        )

        try:

            db.register_user(

                username,

                email,

                hashed_password,

                role

            )

            return True

        except Exception:

            return False

    ########################################################

    def login(

        self,

        email,

        password

    ):

        db.cursor.execute(

            """

            SELECT *

            FROM users

            WHERE email=?

            """,

            (

                email,

            )

        )

        user = db.cursor.fetchone()

        if user is None:

            return None

        stored_password = user[3]

        if self.verify_password(

            password,

            stored_password

        ):

            return {

                "id": user[0],

                "username": user[1],

                "email": user[2],

                "role": user[4]

            }

        return None

    ########################################################

    def is_hr(

        self,

        user

    ):

        if user:

            return user["role"] == "HR"

        return False

    ########################################################

    def is_applicant(

        self,

        user

    ):

        if user:

            return user["role"] == "Applicant"

        return False


auth = Authentication()
