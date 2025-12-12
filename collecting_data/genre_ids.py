import requests
import json
from dotenv import load_dotenv
import os
import sqlite3

load_dotenv()
TMDB_KEY = os.getenv("TMDB_KEY")
if not TMDB_KEY:
    raise SystemExit("TMDB_KEY not found")

def genre_ids():
    """
    Desc: Getting a list of all genre_ids and genre names and putting them in a new table.
    """

    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()

    genres = data.get("genres", [])
    cleaned_genres = []
    
    for genre in genres:
        cleaned_genres.append({
            "genre_id": genre["id"],
            "genre": genre["name"]
        })

    conn = sqlite3.connect("peanuts.db")
    c = conn.cursor()

    #making table to put the values in.
    c.execute("""
    CREATE TABLE IF NOT EXISTS genres(
        genre_id INTEGER NOT NULL,
        genre TEXT NOT NULL,
        UNIQUE(genre_id)
    )""")

    #inserting the ids and names.
    for genre in cleaned_genres:
        c.execute("""
        INSERT OR IGNORE INTO genres (genre_id, genre)
        VALUES (:genre_id, :genre)
        """, genre)
    
    conn.commit()
    conn.close()