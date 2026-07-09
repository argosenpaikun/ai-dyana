import redis


_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True,
)


def get_redis():
    """
    Return the Redis client.
    """
    return _client