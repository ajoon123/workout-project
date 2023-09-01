from user import User, Measurement
from utils import load_user_profiles_from_file

class FitnessTracker:
    def __init__(self, user_profiles_filename):
        self.user_profiles = self.load_user_profiles(user_profiles_filename)

    def load_user_profiles(self, user_profiles_filename):
        user_profiles_data = load_user_profiles_from_file(user_profiles_filename)
        user_profiles = [self.create_user(profile) for profile in user_profiles_data]
        return user_profiles

    def create_user(self, profile):
        measurements = [Measurement(m["date"], m["weight"], m["body_fat"]) for m in profile["measurements"]]
        user = User(
            profile["username"],
            profile["name"],
            profile["age"],
            profile["height"],
            profile["weight"],
            profile["goals"],
            measurements
        )
        return user
