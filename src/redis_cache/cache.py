import json

from redis_cache.client import get_redis


def get_cached_answer(
    question: str,
):
    """
    Return cached answer if it exists.
    """
    redis = get_redis()

    data = redis.get(question)

    if data is None:
        return None

    return json.loads(data)


def cache_answer(
    question: str,
    answer: dict,
):
    """
    Store answer in Redis.
    """
    redis = get_redis()

    redis.set(
        question,
        json.dumps(answer),
    )


def delete_cached_answer(
    question: str,
):
    """
    Delete cached answer.
    """
    redis = get_redis()

    redis.delete(question)


def clear_cache():
    """
    Remove all cached entries.
    """
    redis = get_redis()

    redis.flushdb()