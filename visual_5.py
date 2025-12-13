import sqlite3
import matplotlib.pyplot as plt

#connect db.
conn = sqlite3.connect("peanuts.db")
c = conn.cursor()

c.execute("""
    SELECT 
        g.genre,
        COUNT(*) AS count
    FROM movies AS m
    JOIN genres AS g
      ON m.genre_id = g.genre_id
    GROUP BY g.genre
    ORDER BY count ASC
""")
rows = c.fetchall()
conn.close()

genres = []
counts = []

for row in rows:
    genres.append(row[0])
    counts.append(row[1])

#plot
plt.figure(figsize=(10, 5))
plt.barh(genres, counts, alpha=0.5, color="purple")
plt.xlabel("Movie counts per genre")
plt.title("Distribution of Genres in Top 5 Movies since 2000 to 2024.")
plt.tight_layout()
plt.show()