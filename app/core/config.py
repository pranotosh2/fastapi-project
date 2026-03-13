import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME="Car Price Prediction API"
    
    API_KEY=os.getenv("API_KEY", "default_api_key")
    
    JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY",'default_jwt_secret_key')
    JWT_ALGORITHM='HS256'
    REDIS_URL=os.getenv("REDIS_URL", "redis://localhost:6379")
    MOSEL_PATH='app/models/model.pkl'
    
settings = Settings()
    