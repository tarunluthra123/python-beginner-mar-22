# movie1 = "The Dark Knight"
# movie2 = "The Godfather"
# movie3 = "The Godfather: Part II"
# movie4 = "The Godfather: Part III"
# movie5 = "Lord of the Rings: The Return of the King"


godfather_trilogy = [
    "The Godfather",
    "The Godfather: Part II",
    "The Godfather: Part III",
]

# Create a list of the movies
movies = [
    "The Dark Knight",
    godfather_trilogy,
    "Lord of the Rings: The Return of the King",
    300,
    2.0,
    "The Dark Knight",
]

print(movies)
print(movies[0])  # The Dark Knight
print(movies[4])  # 2.0
print(
    movies[1]
)  # ["The Godfather", "The Godfather: Part II", "The Godfather: Part III"]
print(movies[1][1])  # The Godfather: Part II
print(movies[1][2])  # The Godfather: Part III


# print(movies[50]) -> Error
print(movies[0], movies[2])
