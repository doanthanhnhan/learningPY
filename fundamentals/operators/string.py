# Comparison Operators
print('a' < 'b')  # 'a' has a smaller Unicode value

house = "Gryffindor"
house_copy = "Gryffindor"

print(house == house_copy)

new_house = "Slytherin"

print(house == new_house)

print(new_house <= house)

print(new_house >= house)

# Concatenation
first_half = "Bat"
second_half = "man"

full_name = first_half + second_half
print(full_name)

# The * operator allows us to multiply a string, resulting in a repeating pattern:
print("ha" * 3)

# Search
# The in keyword can be used to check if a particular substring exists in another string.
# If the substring is found, the operation returns true.
random_string = "This is a random string"

print('of' in random_string)  # Check whether 'of' exists in randomString
print('random' in random_string)  # 'random' exists!
