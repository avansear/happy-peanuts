from collecting_data.fetch_games import fetch_games_by_year
from collecting_data.clean_games import clean_games
from collecting_data.insert_games import insert_games
from collecting_data.fetch_movies import fetch_movies_by_year
from collecting_data.clean_movies import clean_movies
from collecting_data.insert_movies import insert_movies
import json

def main():
    for i in range(2000, 2025):
        raw_movies = fetch_movies_by_year(i)
        raw_games = fetch_games_by_year(i)
        cleaned_movies = clean_movies(raw_movies)
        cleaned_games = clean_games(raw_games)
        insert_movies(cleaned_movies)
        insert_games(cleaned_games)
    
    print("check peanuts.db")

if __name__ == "__main__":
    main()