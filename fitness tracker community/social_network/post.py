from datetime import datetime

class Post:
    def __init__(self, username, content):
        self.username = username
        self.timestamp = datetime.now()
        self.content = content

    def __str__(self):
        return f"{self.timestamp} - {self.username}: {self.content}"
