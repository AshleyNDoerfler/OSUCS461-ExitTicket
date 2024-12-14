from OSUCS461.Classes.Database.__init__ import DB

class Post:
    def __init__(self, post_id, user_id, content):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content

    @staticmethod
    def get_posts_by_user_id(user_id):
        query = "SELECT * FROM posts WHERE user_id = %s"
        results = DB.query(query, (user_id,))
        return [Post(*row) for row in results]

    def save(self):
        query = "INSERT INTO posts (post_id, user_id, content) VALUES (%s, %s, %s)"
        DB.execute(query, (self.post_id, self.user_id, self.content))
