from user_profile import UserProfile
from encryption import generate_salt, generate_password_hash, verify_password
from utils import load_user_profiles_from_file, save_user_profiles_to_file

class UserManager:
    

    def authenticate_user(self, username, password):
        user = self.get_user_by_username(username)
        if user and verify_password(password, user.salt, user.password_hash):
            return user
        return None

    def register_user(self, username, password, name, age, email):
        if self.get_user_by_username(username):
            return False
        salt = generate_salt()
        password_hash = generate_password_hash(password, salt)
        new_user = UserProfile(username, password_hash, salt, name, age, email)
        self.user_profiles.append(new_user)
        self.save_user_profiles()
        return True
