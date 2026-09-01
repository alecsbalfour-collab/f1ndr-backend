import os
from dotenv import load_dotenv

load_dotenv()

class Env:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

env = Env()
