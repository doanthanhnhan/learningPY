# The while Loop in Action
n = 2  # Could be any number
power = 0
val = n
while val < 1000:
  power += 1
  val *= n
print(power)

# =================
n = 249
last = n % 10  # Finding the last number is easy

first = n  # Set it to `n` initially
while first >= 10:
  first //= 10  # Keep dividing by 10 until the leftmost digit is reached.

result = first + last
print(result)

# Cautionary Measures
# while (True):
#   print("Hello World")

x = 1
while (x > 0):
  x += 5
