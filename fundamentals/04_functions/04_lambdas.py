# Definition
# A lambda is an anonymous function that returns some form of data.
# Syntax
triple = lambda num: num * 3  # Assigning the lambda to a variable

print(triple(10))  # Calling the lambda and giving it a parameter

concat_strings = lambda a, b, c: a[0] + b[0] + c[0]

print(concat_strings("World", "Wide", "Web"))

my_func = lambda num: "High" if num > 50 else "Low"

print(my_func(60))

# my_func = lambda num: "High" if num > 50 <== error

