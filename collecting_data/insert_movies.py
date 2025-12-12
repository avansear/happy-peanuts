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
        votes INTEGER,
        rank INTEGER CHECK(rank BETWEEN 1 and 5),
        genre_id INTEGER,
        FOREIGN KEY(genre_id) REFERENCES genres(genre_id),
        UNIQUE(movie_name, year)
    )""")

    #inserting movies
    for movie in cleaned_movies:
        c.execute("""
        INSERT OR IGNORE INTO movies (movie_name, year, rating, votes, rank, genre_id)
        VALUES (:movie_name, :year, :rating, :votes, :rank, :genre_id)
        """, movie)
    
    conn.commit()
    conn.close()