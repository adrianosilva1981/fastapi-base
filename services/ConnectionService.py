import aiomysql
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

class ConnectionService:
    def __init__(self):
        self.host = os.getenv('DATABASE_HOST')
        self.db = os.getenv('DATABASE_NAME')
        self.user = os.getenv('DATABASE_USER')
        self.password = os.getenv('DATABASE_PASS')
        self.connection = None
        self.cursor = None

    async def connect(self):
        try:
            self.connection = await aiomysql.connect(
                host=self.host,
                db=self.db,
                user=self.user,
                password=self.password,
                autocommit=True
            )

            print("Conexão bem-sucedida ao MariaDB")
            self.cursor = await self.connection.cursor()
        except Exception as e:
            print(f"Erro ao conectar: {e}")
            return None

    async def execute_query(self, query):
        if self.connection is None:
            print("Conexão não estabelecida.")
            return None
        try:
            await self.cursor.execute(query)
            columns = [desc[0] for desc in self.cursor.description]
            raw_data = await self.cursor.fetchall()
            if not columns or not raw_data:
                return [], []
            return columns, raw_data
        except Exception as e:
            print(f"Erro ao executar a query: {e}")
            return None

    async def close(self):
        if self.cursor:
            await self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Conexão encerrada.")
