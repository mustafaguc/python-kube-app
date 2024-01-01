class Post:
    def __init__(self, post_id, title, content):
        self.id = post_id
        self.title = title
        self.content = content

    def __str__(self):
        return f"Post ID: {self.id}\nTitle: {self.title}\nContent: {self.content}"
