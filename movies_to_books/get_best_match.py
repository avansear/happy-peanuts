from movies_to_books.similarity import calculate_similarity

def get_best_book_match(movie, book_results):
    """
    Desc: Returns best matching book from Open Library search results that is the closest to the movie name provided.
    """
    threshold = 80
    best_book = None
    best_score = 0

    for book in book_results:
        book_title = book.get("title", "")