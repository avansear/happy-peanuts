from collecting_data.fetch_games import fetch_games_by_year
from collecting_data.clean_games import clean_games
from collecting_data.insert_games import insert_games
from collecting_data.fetch_movies import fetch_movies_by_year
from collecting_data.clean_movies import clean_movies
from collecting_data.insert_movies import insert_movies
from collecting_data.return_row_count import return_row_count
from collecting_data.year_row_count import year_row_count
import json

def main():
    print("Fetching top videogames and movies from 2000 to 2024.\n")

    games_rows_before = return_row_count("games")
    movies_rows_before = return_row_count("movies")

    print(f"Before:\nMovies: {movies_rows_before}\nVideo Games: {games_rows_before}")

    game_limit = 25
    movie_limit = 25
    inserted_games = 0
    inserted_movies = 0

    for year in range(2000, 2025):
        if inserted_movies < movie_limit:
            current = year_row_count("movies", year)

            if current < 5:
                needed = 5 - current
                raw = fetch_movies_by_year(year)
                cleaned = clean_movies(raw)
                insert_movies(cleaned[:needed])
                inserted_movies += needed
        
        if inserted_games < game_limit:
            current = year_row_count("games", year)

            if current < 5:
                needed = 5 - current
                raw = fetch_games_by_year(year)
                cleaned = clean_games(raw)
                insert_games(cleaned[:needed])
                inserted_games += needed

        if inserted_movies >= movie_limit and inserted_games >= game_limit:
            break
    
    print("\nAdding rows...")

    if year == 2024 and inserted_movies == 0 and inserted_games == 0:
        print("\nCan't run more, limit year 2024 reached.\n")
    else:
        current_game_rows = return_row_count("games")
        current_movie_rows = return_row_count("movies")
        print("\nAdding limit reached (25). Run again to continue.\n")
        print(f"After:\nMovies: {current_movie_rows}\nVideo Games: {current_game_rows}")


if __name__ == "__main__":
    main()