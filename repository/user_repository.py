from core.database import db
from bson import ObjectId 

class UserRepository:

    @staticmethod
    async def find_by_username_or_email(identifier: str):
        return await db.users.find_one({
            "$or": [
                {"username": identifier},
                {"email": identifier}
            ]
        })

    @staticmethod
    async def create_user(user_data: dict):
        result = await db.users.insert_one(user_data)
        user_doc = await db.users.find_one({"_id": result.inserted_id})
        user_doc["_id"] = str(user_doc["_id"]) 
        
        return user_doc