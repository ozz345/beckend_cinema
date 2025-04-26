import json
import requests

class Usersfile:
    def __init__(self):
        self.__file_url = 'https://raw.githubusercontent.com/ozz345/beckend_cinema/main/data/Users.json'

    def get_all_users(self):
        response = requests.get(self.__file_url)
        response.raise_for_status()  # Raise an error if the request failed
        data = response.json()
        return data["users"]

    def add_users(self, obj):
        users = self.get_all_users()
        # Check if user with same ID already exists
        if any(p.get("id") == obj.get("id") for p in users):
            return {"message": "User with this ID already exists"}

        users.append(obj)
        data = {"users": users}

        # 🔥 WARNING: Cannot write directly to GitHub raw URL
        print("New user data would be:", json.dumps(data, indent=4))
        return {"message": "created (but file not actually updated)"}

    def update_user(self, obj, id):
        users = self.get_all_users()
        for i, user in enumerate(users):
            if user.get("id") == id:
                obj["id"] = id
                users[i] = obj
                data = {"users": users}

                print("Updated user data would be:", json.dumps(data, indent=4))
                return {"message": "updated (but file not actually updated)"}
        return {"message": "user not found"}

    def delete_user(self, id):
        try:
            users = self.get_all_users()
            for i, user in enumerate(users):
                if user.get("id") == id:
                    users.pop(i)
                    data = {"users": users}

                    print("User data after deletion would be:", json.dumps(data, indent=4))
                    return {"message": "deleted (but file not actually updated)"}
            return {"message": "user not found"}
        except Exception as e:
            print(f"Error in delete_user file operation: {str(e)}")
            return {"message": "error deleting user", "error": str(e)}
