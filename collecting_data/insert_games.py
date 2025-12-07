import sqlite3

def insert_games(cleaned_games):
    """
    Desc: Taking clean dictionary of games, and inserting into games table in the peanuts database.
    """

    conn = sqlite3.connect("peanuts.db")
    c = conn.cursor()

    #creating table if it doesn't exist with 5 columns
    c.execute("""
    CREATE TABLE IF NOT EXISTS games(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        game_name TEXT NOT NULL,
        year INTEGER NOT NULL,
        rating REAL,
        rank INTEGER CHECK(rank BETWEEN 1 and 10),
        UNIQUE(game_name, year)
    )""")

    #inserting games
    for game in cleaned_games:
        c.execute("""
        INSERT OR IGNORE INTO games (game_name, year, rating, rank)
        VALUES (:game_name, :year, :rating, :rank)
        """, game)
    
    conn.commit()
    conn.close()