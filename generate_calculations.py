"""
Generate calculations.txt from database queries
"""

import sqlite3

conn = sqlite3.connect("peanuts.db")
c = conn.cursor()

#getting all year based data.
c.execute("SELECT year, SUM(votes) FROM movies GROUP BY year ORDER BY year")
movie_votes_rows = c.fetchall()
movie_votes_data = {}
for row in movie_votes_rows:
    year = row[0]
    votes = row[1]
    movie_votes_data[year] = votes

c.execute("SELECT year, SUM(votes) FROM games GROUP BY year ORDER BY year")
game_votes_rows = c.fetchall()
game_votes_data = {}
for row in game_votes_rows:
    year = row[0]
    votes = row[1]
    game_votes_data[year] = votes

c.execute("""
    SELECT year, SUM(CASE WHEN rating >= 8 THEN 1 ELSE 0 END)
    FROM movies
    GROUP BY year
    ORDER BY year
""")
movie_hits_rows = c.fetchall()
movie_hits_data = {}
for row in movie_hits_rows:
    year = row[0]
    hits = row[1]
    movie_hits_data[year] = hits

c.execute("""
    SELECT year, SUM(CASE WHEN rating >= 4 THEN 1 ELSE 0 END)
    FROM games
    GROUP BY year
    ORDER BY year
""")
game_hits_rows = c.fetchall()
game_hits_data = {}
for row in game_hits_rows:
    year = row[0]
    hits = row[1]
    game_hits_data[year] = hits

c.execute("""
    SELECT m.year, m.rating AS movie_rating, g.rating AS game_rating
    FROM movies AS m
    JOIN games AS g ON m.year = g.year
    WHERE m.rank = 1 AND g.rank = 1
    ORDER BY m.year
""")
top_ratings_rows = c.fetchall()
top_ratings_data = {}
for row in top_ratings_rows:
    year = row[0]
    movie_rating = row[1]
    game_rating = row[2] * 2
    top_ratings_data[year] = (movie_rating, game_rating)

#getting rating and votes to make summary.
c.execute("SELECT rating, votes FROM movies")
movies = c.fetchall()
c.execute("SELECT rating, votes FROM games")
games = c.fetchall()

movie_ratings_list = []
movie_votes_list = []
game_ratings_list = []
game_votes_list = []

for row in movies:
    movie_ratings_list.append(row[0])
    movie_votes_list.append(row[1])

for row in games:
    game_ratings_list.append(row[0])
    game_votes_list.append(row[1])
    
#getting genre information to create per-genre list.
c.execute("""
    SELECT g.genre, COUNT(*) AS count
    FROM movies AS m
    JOIN genres AS g ON m.genre_id = g.genre_id
    GROUP BY g.genre
    ORDER BY count DESC
""")
genre_data = c.fetchall()
conn.close()

#writing to calculations.txt file.
f = open("calculations.txt", "w")
f.write("Year-by-Year Data\n\n")
f.write(f"{'Year':<10} {'Movie Votes':<20} {'Game Votes':<20} {'Movie Hits':<20} {'Game Hits':<20} {'Movie Top Rating':<20} {'Game Top Rating':<20}\n")

for year in movie_votes_data.keys():
    mv = movie_votes_data.get(year, 0)
    gv = game_votes_data.get(year, 0)
    mh = movie_hits_data.get(year, 0)
    gh = game_hits_data.get(year, 0)
    mtr, gtr = top_ratings_data[year]
    f.write(f"{year:<10} {mv:<20,} {gv:<20,} {mh:<20,} {gh:<20,} {mtr:<20,.2f} {gtr:<20,.2f}\n")

f.write(f"\n")
f.write(f"="*200)

f.write(f"\n\nSummary Statistics\n\n")
f.write(f"{'Category':<20} {'Average Rating':<20} {'Total Votes':<20}\n")
f.write(f"{'Movies':<20} {sum(movie_ratings_list)/len(movie_ratings_list):<20,.2f} {sum(movie_votes_list):<20,}\n")
game_avg_rating = (sum(game_ratings_list)/len(game_ratings_list)) * 2
f.write(f"{'Games':<20} {game_avg_rating:<20,.2f} {sum(game_votes_list):<20,}\n\n")

f.write(f"="*200)

f.write(f"\n\nMovies Genre Distribution\n\n")
f.write(f"{'Genre':<20} {'Count':<20}\n")
for genre, count in genre_data:
    f.write(f"{genre:<20} {count:<20,}\n")

f.close()

print("Calculations outputted to a text file.")