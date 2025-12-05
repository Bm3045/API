import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(BASE_DIR, "data_cache.json")
API_BASE_URL = "https://jsonplaceholder.typicode.com"
ENDPOINTS = {
    "posts": "/posts",
    "users": "/users"
}
TIMEOUT = 10  # seconds