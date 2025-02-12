
class JwtService:
    def __init__(self):
        with open("private.pem", "r") as f:
            PRIVATE_KEY = f.read()
        with open("public.pem", "r") as f:
            PUBLIC_KEY = f.read()