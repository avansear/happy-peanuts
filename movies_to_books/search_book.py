import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_KEY = os.getenv("GOOGLE_KEY")
if not GOOGLE_KEY:
    raise SystemExit("GOOGLE_KEY not found")

def search_books_for_movies(norm_title):
    """
    Desc: Takes normalized movie titles, and finds the book for it, using Open Library
    """

    #converting spaces to + 
    params = norm_title.replace(" ", "+")

    url = f"https://www.googleapis.com/books/v1/volumes?q={params}&maxResults=25&key={GOOGLE_KEY}"    
    response = requests.get(url)
    data = response.json()
    return data.get("docs", [])