import sqlite3
import matplotlib.pyplot as plt

#connect db.
conn = sqlite3.connect("peanuts.db")
c = conn.cursor()

#getting only movies and games that are rank 1 for every year. (using JOIN)
c.execute("""
    SELECT 
        m.year,
        m.rating AS movie_rating,
        g.rating AS game_rating
    FROM movies AS m
    JOIN games  AS g
      ON m.year = g.year
    WHERE m.rank = 1
      AND g.rank = 1
    ORDER BY m.year
""")
rows = c.fetchall()
conn.close()

years = []
movie_best = []
game_best = []

for row in rows:
    years.append(row[0])
    movie_best.append(row[1])
    game_best.append(row[2]*2) #multiplying by 2 so both ratings are out of 10.

#plot
plt.figure(figsize=(10, 5))
plt.plot(years, movie_best, label="Top Movie", alpha=0.5, color="purple")
plt.plot(years, game_best, label="Top Game", alpha=0.5, color="red")
plt.xlabel("Year")
plt.ylabel("Rating")
plt.title("Top Movie vs Top Game Rating since 2000 to 2024")
plt.ylim(0, 10)
plt.legend()
plt.show()