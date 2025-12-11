import sqlite3
import matplotlib.pyplot as plt
import numpy as np

#connecting db
conn = sqlite3.connect("peanuts.db")
c = conn.cursor()

#getting all movies ratings, and vote counts.
c.execute("SELECT rating, votes FROM movies")
movies = c.fetchall()

#getting all games ratings, and vote counts.
c.execute("SELECT rating, votes FROM games")
games = c.fetchall()

conn.close()

#putting movie data from tables into lists.
movie_ratings = []
movie_votes = []
for row in movies:
    rating = row[0]
    votes = row[1]
    movie_ratings.append(rating)
    movie_votes.append(votes)

#putting movie data from tables into lists.
game_ratings = []
game_votes = []
for row in games:
    rating = row[0]
    votes = row[1]
    game_ratings.append(rating)
    game_votes.append(votes)

# Scale votes to 0-100 range (relative to each industry's max)
movie_votes_array = np.array(movie_votes)
game_votes_array = np.array(game_votes)
movie_votes_rel = np.interp(movie_votes_array, (0, movie_votes_array.max()), (0, 100))
game_votes_rel = np.interp(game_votes_array, (0, game_votes_array.max()), (0, 100))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

#movies
ax1.scatter(movie_ratings, movie_votes_rel, alpha=0.5, color="purple")
ax1.set_title("Relative Popularity vs. Ratings for Movies on TMDB")
ax1.set_xlabel("Rating")
ax1.set_ylabel("Popularity")

#games
ax2.scatter(game_ratings, game_votes_rel, alpha=0.5, color="red")
ax2.set_title("Relative Popularity vs. Ratings for Games on RAWG")
ax2.set_xlabel("Rating")
ax1.set_ylabel("Popularity")

#plotting
fig.suptitle("Relative Popularity vs. Ratings for Movies and Games")
plt.show()