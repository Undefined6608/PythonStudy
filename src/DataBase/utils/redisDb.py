import redis

def get_conn():
    return redis.Redis(
        host="127.0.0.1",
        port=6379,
        password="6728d0b3-b77d-4783-896a-b8a6be7c87ad",
        db=3
    )