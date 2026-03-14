import json
import redis

from app.core.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)

def get_cached_prediction(key: str):
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data)
    return None


def set_cached_prediction(key: str, value: dict, expiration: int = 3600):
    redis_client.setex(key, expiration, json.dumps(value))