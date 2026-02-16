import os
from dotenv import load_dotenv


load_dotenv()

class settings:
    PROJECT_NAME = 'car Price API'
    API_KEY = os.getenv('API_KEY', 'demo-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'demo-secret-key')
    JWT_ALGORITHM = 'HS256'
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    MODEL_PATH = 'app/models/model.pkl'

settings = settings()