import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
TMDB_KEY = os.getenv("TMDB_KEY")
if not TMDB_KEY:
    raise SystemExit("TMDB_KEY not found")

def fetch_movies_by_year(year):
    """
    Desc: Fetching top movies for given year from TMDB, in raw form.
    """

    #url that has api key, filters movies by release year, minimum 500 reviews, and sorts by popularity in descending order.
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_KEY}&sort_by=popularity.desc&primary_release_year={year}&vote_count.gte=500"
    response = requests.get(url)
    data = response.json()

    return data