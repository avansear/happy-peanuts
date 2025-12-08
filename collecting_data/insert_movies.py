import sqlite3

def insert_movies(cleaned_movies):
    """
    Desc: Taking clean dictionary of movies, and inserting into movies table in the peanuts database.
    """

    conn = sqlite3.connect("peanuts.db")
    c = conn.cursor()

    #creating table if it doesn't exist with 5 columns
    c.execute("""
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_name TEXT NOT NULL,
        year INTEGER NOT NULL,
        rating REAL,
        rank INTEGER CHECK(rank BETWEEN 1 and 10),
        UNIQUE(movie_name, year)
    )""")

    #inserting movies
    for movie in cleaned_movies:
        c.execute("""
        INSERT OR IGNORE INTO movies (movie_name, year, rating, rank)
        VALUES (:movie_name, :year, :rating, :rank)
        """, movie)
    
    conn.commit()
    conn.close()