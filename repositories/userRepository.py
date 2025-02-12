from services.ConnectionService import ConnectionService
from utils.mapToJson import mapToJson
from dotenv import load_dotenv

load_dotenv()

async def getUsers():
    db = ConnectionService()
    await db.connect()

    query = 'SELECT * FROM users'
    columns, users = await db.execute_query(query)
    return mapToJson(users, columns)


async def setUser():
    db = ConnectionService()
    await db.connect()

    query = 'INSERT INTO...'
    columns, users = await db.execute_query(query)
    return mapToJson(users, columns)