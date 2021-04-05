# Strings
# Search
# a_string.find(substring, start, end)
random_string = "This is a string"
print(random_string.find("is"))  # First instance of 'is' occurs at index 2
print(random_string.find("is", 9, 13))  # No instance of 'is' in this range

# Replace
# a_string.replace(substring_to_be_replace, new_string)
a_string = "Welcome to Educative!"
new_string = a_string.replace("Welcome to", "Greetings from")
print(a_string)
print(new_string)

# Changing the Letter Case
# In Python, the letter case of a string can be easily changed using the upper() and lower() methods.
print("UpperCase".upper())
print("LowerCase".lower())

# Type Conversions
print(int("12") * 10)  # String to integer
print(int(20.5))  # Float to integer
print(int(False))  # Bool to integer

# print (int("Hello")) # This wouldn't work!

print(ord('a'))
print(ord('0'))

print(float(24))
print(float('24.5'))
print(float(True))

print(str(12) + '.345')
print(str(False))
print(str(12.345) + ' is a string')

print(bool(10))
print(bool(0.0))
print(bool("Hello"))
print(bool(""))
