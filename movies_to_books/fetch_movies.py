import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
TMDB_KEY = os.getenv("TMDB_KEY")
if not TMDB_KEY:
    raise SystemExit("TMDB_KEY not found")

def fetch_movies(page):
    """
    Desc: Takes page number and returns a JSON which contains movies, filtered by popularity in descending order.
    """

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_KEY}&sort_by=popularity.desc&page={page}"
    response = requests.get(url)
    data = response.json()

    return data
    pass