from movies_to_books.fetch_movies import fetch_movies
from movies_to_books.clean_movies import clean_movies
from movies_to_books.normalize_title import normalize_title
from movies_to_books.search_book import search_books_for_movies
import json

raw = fetch_movies(page=1)
cleaned = clean_movies(raw)
normalized = normalize_title(cleaned)
book_results = search_books_for_movies(normalized[0]["title"])

print(json.dumps(book_results, indent=4))
