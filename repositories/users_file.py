import json
import requests
from pymongo import MongoClient
from bson import ObjectId

class Usersfile:
    def __init__(self):
        self.__file = 'https://raw.githubusercontent.com/ozz345/beckend_cinema/main/data/Users.json'
        # MongoDB connection
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['cinema_db']
        self.users_collection = self.db['users']

    def get_all_users(self):
        try:
            # First try to get from MongoDB
            mongo_users = list(self.users_collection.find({}, {'_id': 0}))
            if mongo_users:
                return mongo_users

            # If MongoDB is empty, try GitHub as backup
            try:
                response = requests.get(self.__file)
                response.raise_for_status()  # Raise an exception for bad status codes
                data = response.json()
                return data["users"]
            except requests.exceptions.RequestException as e:
                print(f"Error fetching from GitHub: {str(e)}")
                return []
        except Exception as e:
            print(f"Error in get_all_users: {str(e)}")
            return []

    def add_users(self, obj):
        try:
            # Check if user with same ID already exists in MongoDB
            existing_user = self.users_collection.find_one({"id": obj.get("id")})
            if existing_user:
                return {"message": "User with this ID already exists"}

            # Add the new user to MongoDB
            self.users_collection.insert_one(obj)
            return {"message": "created"}
        except Exception as e:
            print(f"Error adding user: {str(e)}")
            return {"message": "error adding user"}

    def update_user(self, obj, id):
        try:
            # Update user in MongoDB
            result = self.users_collection.update_one(
                {"id": id},
                {"$set": obj}
            )

            if result.modified_count > 0:
                return {"message": "updated"}
            return {"message": "user not found"}
        except Exception as e:
            print(f"Error updating user: {str(e)}")
            return {"message": "error updating user"}

    def delete_user(self, id):
        try:
            # Delete user from MongoDB
            result = self.users_collection.delete_one({"id": id})

            if result.deleted_count > 0:
                return {"message": "deleted"}
            return {"message": "user not found"}
        except Exception as e:
            print(f"Error in delete_user operation: {str(e)}")
            return {"message": "error deleting user", "error": str(e)}
