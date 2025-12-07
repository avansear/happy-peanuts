from movies_to_books.fetch_movies import fetch_movies
from movies_to_books.clean_movies import clean_movies
import json

raw = fetch_movies(page=1)
cleaned = clean_movies(raw)

print(json.dumps(cleaned, indent=4))