from motor.motor_asyncio import AsyncIOMotorClient
from .core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)
database = client.my_database