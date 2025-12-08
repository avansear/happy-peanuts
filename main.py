from collecting_data.fetch_games import fetch_games_by_year
from collecting_data.clean_games import clean_games
from collecting_data.insert_games import insert_games
from collecting_data.fetch_movies import fetch_movies_by_year
from collecting_data.clean_movies import clean_movies
import json

def main():
    a = fetch_movies_by_year(2022)
    b = clean_movies(a)
    print(b)

if __name__ == "__main__":
    main()