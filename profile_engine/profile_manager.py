import json
import os

from profile_engine.profile_schema import DEFAULT_PROFILE

PROFILE_PATH = "data/teacher_profile.json"


class ProfileManager:

    def __init__(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(PROFILE_PATH):

            with open(PROFILE_PATH, "w") as f:
                json.dump(DEFAULT_PROFILE, f, indent=2)

    def load_profile(self):

        with open(PROFILE_PATH, "r") as f:
            return json.load(f)

    def save_profile(self, profile):

        temp_path = PROFILE_PATH + ".tmp"

        with open(temp_path, "w") as f:
            json.dump(profile, f, indent=2)

        os.replace(temp_path, PROFILE_PATH)

    def get_profile(self):

        return self.load_profile()

    def update_profile(self, updates):

        profile = self.load_profile()

        self.deep_update(profile, updates)

        self.save_profile(profile)

        return profile

    def deep_update(self, original, updates):

        for key, value in updates.items():

            if isinstance(value, dict):
                self.deep_update(original[key], value)
            else:
                original[key] = value
                
    def set_field(self, path, value):

        profile = self.load_profile()

        keys = path.split(".")

        current = profile

        for key in keys[:-1]:
            current = current.setdefault(key, {})

        current[keys[-1]] = value

        self.save_profile(profile)

        return profile


    def add_to_list(self, path, value):

        profile = self.load_profile()

        keys = path.split(".")

        current = profile

        for key in keys[:-1]:
            current = current.setdefault(key, {})

        final_key = keys[-1]

        if final_key not in current:
            current[final_key] = []

        if value not in current[final_key]:
            current[final_key].append(value)

        self.save_profile(profile)

        return profile