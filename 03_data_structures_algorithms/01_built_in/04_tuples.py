# A tuple is very similar to a list, except for the fact that its contents cannot be changed.
# In other words, a tuple is immutable.
# However, it can contain mutable elements like a list. These elements can be altered.

# Creating a Tuple
car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])

# Merging Tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)

# Nested Tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

# Search
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)

# index()
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))
