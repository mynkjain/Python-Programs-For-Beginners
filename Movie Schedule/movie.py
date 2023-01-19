# List of movies
current_movies = {
    "RRR": "10:00am",
    "Snowden": "1:00pm",
    "Spiderman":"3:00pm",
    "The Batman":"5:30pm"
}

print("We are showing following movies \n")
for movie_key in current_movies:
    print(movie_key)

movie_choice = input("What movie would you like the showtime for \n")

showtime = current_movies.get(movie_choice)

if showtime:
    print(movie_choice,"playing at", current_movies[movie_choice])
else:
    print("Requested movie is not playing")
