# Using a Nested for Loop
n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]

for n1 in num_list:
  for n2 in num_list:  # Now we have two iterators
    if (n1 + n2 == n):
      print(n1, n2)

# The break Keyword
n = 50
num_list = [10, 4, 23, 6, 18, 27, 47]
found = False  # This bool will become true once a pair is found

for n1 in num_list:
  for n2 in num_list:
    if (n1 + n2 == n):
      found = True  # Set found to True
      break  # Break inner loop if a pair is found
  if found:
    print(n1, n2)  # Print the pair
    break  # Break outer loop if a pair is found

# The continue Keyword
num_list = list(range(0, 10))

for num in num_list:
  if num == 3 or num == 6 or num == 8:
    continue
  print(num)

# The pass Keyword
# In all practical meaning, the pass statement does nothing to the code execution.
# It can be used to represent an area of code that needs to be written.
# Hence, it is simply there to assist you when you haven’t written a piece of code
# but still need your entire program to execute.
num_list = list(range(20))

for num in num_list:
  pass  # You can write code here later on

print(len(num_list))
