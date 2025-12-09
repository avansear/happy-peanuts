import requests
from dotenv import load_dotenv
import os

load_dotenv()
RAWG_KEY = os.getenv("RAWG_KEY")

def fetch_games_by_year(year):
    """
    Desc: Fetching top games for given year from RAWG, in raw form.
    """
    url = f"https://api.rawg.io/api/games?key={RAWG_KEY}&dates={year}-01-01,{year}-12-31&ordering=-ratings_count&page_size=10"
    response = requests.get(url)
    data = response.json()

    return data["results"]