# A Simple Example
def rec_count(number):
  print(number)
  # Base case
  if number == 0:
    return 0
  rec_count(number - 1)  # A recursive call with a different argument
  print(number)


rec_count(5)


# A Complex Example
# The Fibonacci sequence is a popular series of numbers in mathematics,
# where every number is the sum of the two numbers before it.
# The first two terms in the series are 0 and 1:
# 0 1 1 2 3 5 8 13
# Let’s write a function which takes in a number, n,
# and returns the nth number in the Fibonacci sequence.
# So, if n == 6, the function will return 5:
def fib(n):
  fi = [0, 1]
  # The base cases
  for i in range(2, n + 1):
    # Recursive call
    fi.append(fib(n - 1) + fib(n - 2))
  return fi[n]


print(fib(10))
