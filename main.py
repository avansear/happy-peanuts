from movies_to_books.fetch_movies import fetch_movies
from movies_to_books.clean_movies import clean_movies
from movies_to_books.normalize_title import normalize_title
import json

raw = fetch_movies(page=1)
cleaned = clean_movies(raw)
normalized = normalize_title(cleaned)

print(json.dumps(normalized, indent=4))