from collecting_data.fetch_games import fetch_games_by_year
from collecting_data.clean_games import clean_games
from collecting_data.insert_games import insert_games

def main():
    for year in range(2000, 2025):
        raw = fetch_games_by_year(year)
        cleaned = clean_games(raw)
        insert_games(cleaned)
        
    print("Check peanuts.db")

if __name__ == "__main__":
    main()