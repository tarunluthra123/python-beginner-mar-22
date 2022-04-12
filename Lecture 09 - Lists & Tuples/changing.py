planets = (
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
)
# Step 1: Convert tuple to a list
original_planets = planets
planets = list(planets)

# Step 2: Change the data inside the list
planets.append("Pluto")

# Step 3: Convert the list back to a tuple
planets = tuple(planets)

print(planets)
print(type(planets))
