import sqlite3
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect("peanuts.db")
c = conn.cursor()

# Get all yearly totals
c.execute("SELECT year, SUM(votes) FROM movies GROUP BY year ORDER BY year")
m_rows = c.fetchall()
c.execute("SELECT year, SUM(votes) FROM games GROUP BY year ORDER BY year")
g_rows = c.fetchall()
conn.close()

# putting movie data from tables into lists
movie_years = []
movie_total_votes = []
for row in m_rows:
    movie_years.append(row[0])
    movie_total_votes.append(row[1])

# putting game data from tables into lists
game_years = []
game_total_votes = []
for row in g_rows:
    game_years.append(row[0])
    game_total_votes.append(row[1])

movie_total_votes = np.array(movie_total_votes)
game_total_votes = np.array(game_total_votes)

# Scale each medium to 1-100 range (separate scaling to compare trends)
movie_scaled = np.interp(movie_total_votes, (movie_total_votes.min(), movie_total_votes.max()), (1, 100))
game_scaled = np.interp(game_total_votes, (game_total_votes.min(), game_total_votes.max()), (1, 100))

# plot
plt.figure(figsize=(15, 5))
plt.fill_between(movie_years, movie_scaled, alpha=0.5, color="purple", label="Movies")
plt.fill_between(game_years, game_scaled, alpha=0.5, color="red", label="Games")
plt.xlabel("Year")
plt.ylabel("Total Vote Counts")
plt.title("Engagement trends over the years")
plt.legend()
plt.show()