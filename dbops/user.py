from .base import Base


class user(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "users")

    def create(self, user):

        self.cursor.execute(
            "INSERT INTO users VALUES(NULL, ?, ?)",
            (
                user["email"],
                user["password"],
            ),
        )
        self.conn.commit()

    def update(self, user):
        self.cursor.execute(
            "UPDATE users SET email=?, password=? WHERE id=?",
            (
                user["email"],
                user["password"],
                user["id"],
            ),
        )
        self.conn.commit()

    def get_by_email(self, email):
        User = {}
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE email=?", (email,)
            )
            row = self.cursor.fetchone()
            User["email"] = row["email"]
            User["password"] = row["password"]
            User["id"] = row["id"]
        except:
            User = None
        return User

    def get_by_id(self, id):

        User = {}
        try:
            row = super().get_by_id(id)
            User["email"] = row["email"]
            User["password"] = row["password"]
            User["id"] = row["id"]
        except:
            User = None

        return User

    def get_all(self):
        Users = []
        try:
            rows = super().get_all()
            # print(rows)
            for row in rows:
                User = {}
                User["email"] = row["email"]
                User["password"] = row["password"]
                User["id"] = row["id"]
                Users.append(User)
        except:
            Users = None
        return Users


User = user(
    "testing.db",
)
