from redis_cache.cache import (
    cache_answer,
    get_cached_answer,
)

cache_answer(
    "Who developed ChatGPT?",
    {
        "answer": "OpenAI",
    },
)

print(
    get_cached_answer(
        "Who developed ChatGPT?"
    )
)