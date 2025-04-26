import json
import os

class Premissionfile:
    def __init__(self):
        # Get the absolute path to the data directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.__file_path = os.path.join(current_dir, '..', 'data', 'Premission.json')

    def get_all_premissions(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                return data["premissions"]
        except FileNotFoundError:
            return []

    def add_premissions(self, obj):
        premissions = self.get_all_premissions()
        # Check if permission with same ID already exists
        if any(p.get("id") == obj.get("id") for p in premissions):
            return {"message": "Permission with this ID already exists"}

        premissions.append(obj)
        data = {"premissions": premissions}

        try:
            with open(self.__file_path, 'w') as file:
                json.dump(data, file, indent=4)
            return {"message": "Permission created successfully"}
        except Exception as e:
            return {"message": f"Error creating permission: {str(e)}"}

    def update_premissions(self, obj, id):
        premissions = self.get_all_premissions()
        for i, permission in enumerate(premissions):
            if permission.get("id") == id:
                obj["id"] = id
                premissions[i] = obj
                data = {"premissions": premissions}

                try:
                    with open(self.__file_path, 'w') as file:
                        json.dump(data, file, indent=4)
                    return {"message": "Permission updated successfully"}
                except Exception as e:
                    return {"message": f"Error updating permission: {str(e)}"}
        return {"message": "permission not found"}

    def delete_permissions(self, id):
        try:
            premissions = self.get_all_premissions()
            for i, permission in enumerate(premissions):
                if permission.get("id") == id:
                    premissions.pop(i)
                    data = {"premissions": premissions}

                    try:
                        with open(self.__file_path, 'w') as file:
                            json.dump(data, file, indent=4)
                        return {"message": "Permission deleted successfully"}
                    except Exception as e:
                        return {"message": f"Error deleting permission: {str(e)}"}
            return {"message": "permission not found"}
        except Exception as e:
            return {"message": f"Error in delete_permissions operation: {str(e)}"}
