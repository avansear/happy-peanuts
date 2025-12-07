import re

def normalize_title(cleaned_movies):
    """
    Desc: Normalizes movie titles with these steps:
    1. by converting them into lowercase
    2. retains main title by dropping sub title after : symbol
    3. keeping only alpha-numeric characters
    4. strips spaces
    """

    normalized = []

    for movie in cleaned_movies:
        #step 1
        title = movie["title"].lower()

        #using regex to capture both steps 2 and 3
        match = re.search(r"([a-z0-9 ]+)", title)
        if match:
            title = match.group(1)
        else:
            title = ""
        
        #step 4
        title = title.strip()

        #making copy of movie dict, adding a field with new normalized title, and appending it to normalized movies list
        movie_copy = movie.copy()
        movie_copy["normal_title"] = title
        normalized.append(movie_copy)
    
    return normalized