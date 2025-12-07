import requests
import json

def search_books_for_movies(norm_title):
    """
    Desc: Takes normalized movie titles, and finds the book for it, using Open Library
    """

    #converting spaces to + 
    params = norm_title.replace(" ", "+")
    url = f"https://openlibrary.org/search.json?title={params}&limit=25"
    response = requests.get(url)
    data = response.json()

    return data.get("docs", [])