from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://devuser:123456@mongodb:27017/helix")

client = AsyncIOMotorClient(MONGO_URI)
db = client.get_default_database()
