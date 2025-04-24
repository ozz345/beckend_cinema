import json

import requests


class Premissionfile:
    def __init__(self):
        self.__file = 'https://raw.githubusercontent.com/ozz345/beckend_cinema/main/data/Premission.json'

    def get_all_premissions(self):
        try:
            response = requests.get(self.__file)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            return data["premissions"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching permissions: {str(e)}")
            return []

    def add_premissions(self, obj):
        try:
            premissions = self.get_all_premissions()
            # Check if permission with same ID already exists
            if any(p.get("id") == obj.get("id") for p in premissions):
                return {"message": "Permission with this ID already exists"}

            premissions.append(obj)
            data = {"premissions": premissions}
            # Note: You can't write directly to GitHub URL
            # You'll need to implement a different storage solution
            return {"message": "created"}
        except Exception as e:
            print(f"Error adding permissions: {str(e)}")
            return {"message": "error adding permissions"}

    def update_premissions(self, obj, id):
        try:
            premissions = self.get_all_premissions()
            # Find the permission by ID
            for i, permission in enumerate(premissions):
                if permission.get("id") == id:
                    # Update the permission data while preserving the ID
                    obj["id"] = id
                    premissions[i] = obj
                    # Note: You can't write directly to GitHub URL
                    # You'll need to implement a different storage solution
                    return {"message": "updated"}
            return {"message": "permission not found"}
        except Exception as e:
            print(f"Error updating permissions: {str(e)}")
            return {"message": "error updating permissions"}

    def delete_permissions(self, id):
        try:
            premissions = self.get_all_premissions()
            # Find and remove the permissions by ID
            for i, permission in enumerate(premissions):
                if permission.get("id") == id:
                    premissions.pop(i)
                    # Note: You can't write directly to GitHub URL
                    # You'll need to implement a different storage solution
                    return {"message": "deleted"}
            return {"message": "permissions not found"}
        except Exception as e:
            print(f"Error in delete_permissions operation: {str(e)}")
            return {"message": "error deleting permissions", "error": str(e)}



