light = "Red"

if light == "Green":
  print("Go")

elif light == "Yellow":
  print("Caution")

elif light == "Red":
  print("Stop")

else:
  print("Incorrect light signal")

# Multiple elif Statements
num = 5

if num == 0:
  print("Zero")
elif num == 1:
  print("One")
elif num == 2:
  print("Two")
elif num == 3:
  print("Three")
elif num == 4:
  print("Four")
elif num == 5:
  print("Five")
elif num == 6:
  print("Six")
elif num == 7:
  print("Seven")
elif num == 8:
  print("Eight")
elif num == 9:
  print("Nine")

# On the other hand, in if-elif-else, when a condition evaluates to True,
# the rest of the statement’s conditions are not evaluated.
num = 10

if num > 5:
  print("The number is greater than 5")

if num % 2 == 0:
  print("The number is even")

if not num % 2 == 0:
  print("The number is odd")
