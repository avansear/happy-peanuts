def clean_movies(raw_movies):
    """
    Desc: Cleaning up the raw JSON data, and giving a dictionary that contains name, year, rating, and rank for each movie.
    """
    output = []
    results = raw_movies.get("results", [])
    
    for i, movie in enumerate(results):
        title = movie["title"]
        date = movie["release_date"]
        rating = movie["vote_average"]

        movie_year = int(date[:4])

        output.append({
            "movie_name": title,
            "year": movie_year,
            "rating": rating,
            "rank": i + 1
        })
    
    return output