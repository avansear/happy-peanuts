import sqlite3
import matplotlib.pyplot as plt

# connecting db
conn = sqlite3.connect("peanuts.db")
c = conn.cursor()

# getting movie hits per year (rating >= 8)
c.execute("""
    SELECT year, SUM(CASE WHEN rating >= 8 THEN 1 ELSE 0 END)
    FROM movies
    GROUP BY year
    ORDER BY year
""")
movies = c.fetchall()

# getting game hits per year (rating >= 4 on 0–5)
c.execute("""
    SELECT year, SUM(CASE WHEN rating >= 4 THEN 1 ELSE 0 END)
    FROM games
    GROUP BY year
    ORDER BY year
""")
games = c.fetchall()

conn.close()

# putting movie data from tables into lists
movie_years = []
movie_hits = []
for row in movies:
    movie_years.append(row[0])
    movie_hits.append(row[1])

# putting game data from tables into lists
game_years = []
game_hits = []
for row in games:
    game_years.append(row[0])
    game_hits.append(row[1])

# plot
plt.figure(figsize=(10, 5))
plt.plot(movie_years, movie_hits, label="Movies", alpha=0.5, color="purple")
plt.plot(game_years, game_hits, label="Games", alpha=0.5, color="red")
plt.xlabel("Year")
plt.ylabel("Hit Count")
plt.title("Movie and Game Hits per Year (A hit is when rating is > 80%)")
plt.legend()
plt.show()