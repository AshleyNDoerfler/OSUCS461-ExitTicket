from OSUCS461.Classes.Database.__init__ import DB

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    @staticmethod
    def get_user_by_id(user_id):
        query = "SELECT * FROM users WHERE user_id = %s"
        result = DB.query(query, (user_id,))
        if result:
            return User(*result[0])
        return None

    def save(self):
        query = "INSERT INTO users (user_id, username, email) VALUES (%s, %s, %s)"
        DB.execute(query, (self.user_id, self.username, self.email))
