import pandas as pd
import matplotlib.pyplot as plt

n_df = pd.read_csv("/Users/thenkashamas/Downloads/workspace 2/netflix_data.csv")
movie = n_df[n_df["type"] == "Movie"]
movie1 = movie[movie["release_year"] >= 1990]
movie_90 = movie1[movie1["release_year"] < 2000]
dur = movie_90[["duration"]]
plt.hist(dur)
plt.xlabel("Duration (in minutes)")
plt.ylabel("Frequency")
plt.title("Most frequent duration time")
plt.show()
duration = 100
print("duration = " + str(duration))

# Code for the number of short action movies in the 1990s
n_df = pd.read_csv("/Users/thenkashamas/Downloads/workspace 2/netflix_data.csv")
action_movie_90 = movie_90[movie_90["genre"] == "Action"]
short_movie_count = 0
for lab, row in action_movie_90.iterrows():
    if row["duration"] < 90:
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)