from user_management.user import User
from user_management.utils import load_users_from_file

class UserManager:
    def __init__(self, users_filename):
        self.users = self.load_users(users_filename)

    def load_users(self, users_filename):
        users_data = load_users_from_file(users_filename)
        users = [self.create_user(user) for user in users_data]
        return users

    def create_user(self, user_data):
        user = User(
            user_data["username"],
            user_data["name"],
            user_data["age"],
            user_data["height"],
            user_data["weight"],
            user_data["followers"],
            user_data["following"],
            user_data["posts"]
        )
        return user
