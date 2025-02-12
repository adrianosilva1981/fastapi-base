import jwt
import datetime
from fastapi import HTTPException, Request
from dotenv import load_dotenv
import os

load_dotenv()

class JwtService:
    def __init__(self):
        with open(os.getenv('PRIVATE_KEY_PATH'), "r") as f:
            self.privateKey = f.read()
        with open(os.getenv('PUBLIC_KEY_PATH'), "r") as f:
            self.publicKey = f.read()

    def generateToken(self, user: str):
        payload = {
            "sub": user,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, self.privateKey, algorithm='RS256')
        return token

    def verifyToken(self, request: Request):
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise HTTPException(status_code=401, detail='Invalid token')

        token = token.split("Bearer ")[1]

        try:
            payload = jwt.decode(token, self.publicKey, algorithms=['RS256'])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Expired token')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid Token")