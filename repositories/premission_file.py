import json
import requests

class Premissionfile:
    def __init__(self):
        self.__file_url = 'https://raw.githubusercontent.com/ozz345/beckend_cinema/main/data/Premission.json'

    def get_all_premissions(self):
        response = requests.get(self.__file_url)
        response.raise_for_status()  # Raise an error if request failed
        data = response.json()
        return data["premissions"]

    def add_premissions(self, obj):
        premissions = self.get_all_premissions()
        # Check if permission with same ID already exists
        if any(p.get("id") == obj.get("id") for p in premissions):
            return {"message": "Permission with this ID already exists"}

        premissions.append(obj)
        data = {"premissions": premissions}

        # 🔥 WARNING: You cannot write back directly to a GitHub URL via HTTP!
        # You must manually handle uploading updated data somewhere else (like an API endpoint or GitHub Actions).
        print("New permission data would be:", json.dumps(data, indent=4))
        return {"message": "created (but file not actually updated)"}

    def update_premissions(self, obj, id):
        premissions = self.get_all_premissions()
        for i, permission in enumerate(premissions):
            if permission.get("id") == id:
                obj["id"] = id
                premissions[i] = obj
                data = {"premissions": premissions}
                
                print("Updated permission data would be:", json.dumps(data, indent=4))
                return {"message": "updated (but file not actually updated)"}
        return {"message": "permission not found"}

    def delete_permissions(self, id):
        try:
            premissions = self.get_all_premissions()
            for i, permission in enumerate(premissions):
                if permission.get("id") == id:
                    premissions.pop(i)
                    data = {"premissions": premissions}
                    
                    print("Permission data after deletion would be:", json.dumps(data, indent=4))
                    return {"message": "deleted (but file not actually updated)"}
            return {"message": "permission not found"}
        except Exception as e:
            print(f"Error in delete_permissions file operation: {str(e)}")
            return {"message": "error deleting permissions", "error": str(e)}
