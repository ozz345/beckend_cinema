import json
import os

class Usersfile:
    def __init__(self):
        # Get the absolute path to the data directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.__file_path = os.path.join(current_dir, '..', 'data', 'Users.json')

    def get_all_users(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                return data["users"]
        except FileNotFoundError:
            return []

    def add_users(self, obj):
        users = self.get_all_users()
        # Check if user with same ID already exists
        if any(p.get("id") == obj.get("id") for p in users):
            return {"message": "User with this ID already exists"}

        users.append(obj)
        data = {"users": users}

        try:
            with open(self.__file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return {"message": "User created successfully"}
        except Exception as e:
            return {"message": f"Error creating user: {str(e)}"}

    def update_user(self, obj, id):
        users = self.get_all_users()
        for i, user in enumerate(users):
            if user.get("id") == id:
                obj["id"] = id
                users[i] = obj
                data = {"users": users}

                try:
                    with open(self.__file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                    return {"message": "User updated successfully"}
                except Exception as e:
                    return {"message": f"Error updating user: {str(e)}"}
        return {"message": "user not found"}

    def delete_user(self, id):
        try:
            users = self.get_all_users()
            for i, user in enumerate(users):
                if user.get("id") == id:
                    users.pop(i)
                    data = {"users": users}

                    try:
                        with open(self.__file_path, 'w') as file:
                            json.dump(data, file, indent=4)
                        return {"message": "User deleted successfully"}
                    except Exception as e:
                        return {"message": f"Error deleting user: {str(e)}"}
            return {"message": "user not found"}
        except Exception as e:
            return {"message": f"Error in delete_user operation: {str(e)}"}
