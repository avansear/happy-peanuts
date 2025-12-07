def clean_movies(raw_json):
    """
    Desc: Takes raw JSON from fetch_movies.py and cleans the data by checking for movies that have at least 100 votes.
    """
    
    cleaned = []

    #loops thru each movie, and grabs info of each field
    for movie in raw_json.get("results", []):
        title = movie.get("title", "")
        rdate = movie.get("release_date", "")
        votes = movie.get("vote_count", 0)
        rating = movie.get("vote_average", 0.0)

        #filter to skip empty titles, empty dates, or if review counts are less tha 100
        if not title:
            continue
        if not rdate:
            continue
        if votes < 100:
            continue
        
        year = int(rdate[:4])
        rating = round(rating,2)

        #appending clean data to cleaned list
        cleaned.append({
            "title": title,
            "release_year": year,
            "rating": rating,
            "votes": votes
        })
    
    return cleaned