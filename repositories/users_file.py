
import json

import requests

class Premissionfile:
    def __init__(self):
        self.__file = 'https://raw.githubusercontent.com/ozz345/beckend_cinema/main/data/Premission.json'

    def get_all_users(self):
        try:
            response = requests.get(self.__file)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            return data["users"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching users: {str(e)}")
            return []

    def add_users(self, obj):
        try:
            users = self.get_all_users()
            # Check if permission with same ID already exists
            if any(p.get("id") == obj.get("id") for p in users):
                return {"message": "Permission with this ID already exists"}

            users.append(obj)
            data = {"users": users}
            # Note: You can't write directly to GitHub URL
            # You'll need to implement a different storage solution
            return {"message": "created"}
        except Exception as e:
            print(f"Error adding user: {str(e)}")
            return {"message": "error adding user"}

    def update_user(self, obj, id):
        try:
            users = self.get_all_users()
            # Find the user by ID
            for i, user in enumerate(users):
                if user.get("id") == id:
                    # Update the user data while preserving the ID
                    obj["id"] = id
                    users[i] = obj
                    # Note: You can't write directly to GitHub URL
                    # You'll need to implement a different storage solution
                    return {"message": "updated"}
            return {"message": "user not found"}
        except Exception as e:
            print(f"Error updating user: {str(e)}")
            return {"message": "error updating user"}

    def delete_permissions(self, id):
        try:
            users = self.get_all_users()
            # Find and remove the user by ID
            for i, user in enumerate(users):
                if user.get("id") == id:
                    users.pop(i)
                    # Note: You can't write directly to GitHub URL
                    # You'll need to implement a different storage solution
                    return {"message": "deleted"}
            return {"message": "permissions not found"}
        except Exception as e:
            print(f"Error in delete_user operation: {str(e)}")
            return {"message": "error deleting user", "error": str(e)}



