from user_profile import UserProfile
from utils import load_user_profiles_from_file, save_user_profiles_to_file

class UserManager:
    def __init__(self, users_filename):
        self.users_filename = users_filename
        self.user_profiles = self.load_user_profiles()

    def load_user_profiles(self):
        user_profiles_data = load_user_profiles_from_file(self.users_filename)
        user_profiles = [UserProfile(**profile) for profile in user_profiles_data]
        return user_profiles

    def save_user_profiles(self):
        user_profiles_data = [{"username": profile.username, "password": profile.password, "name": profile.name, "age": profile.age, "email": profile.email} for profile in self.user_profiles]
        save_user_profiles_to_file(self.users_filename, user_profiles_data)

    def get_user_by_username(self, username):
        for profile in self.user_profiles:
            if profile.username == username:
                return profile
        return None

    def authenticate_user(self, username, password):
        user = self.get_user_by_username(username)
        if user and user.password == password:
            return user
        return None

    def register_user(self, username, password, name, age, email):
        if self.get_user_by_username(username):
            return False
        new_user = UserProfile(username, password, name, age, email)
        self.user_profiles.append(new_user)
        self.save_user_profiles()
        return True
