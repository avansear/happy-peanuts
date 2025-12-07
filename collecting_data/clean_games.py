def clean_games(raw_games):
    """
    Desc: Cleaning up the raw JSON data, and giving a dictionary that contains name, year, rating, and rank for each game.
    """
    output = []
    
    for i, game in enumerate(raw_games):
        title = game["name"]
        date = game["released"]
        rating = game["rating"]
        
        # Extract year from date
        game_year = int(date[:4])
        
        output.append({
            "game_name": title,
            "year": game_year,
            "rating": rating,
            "rank": i + 1
        })
    
    return output