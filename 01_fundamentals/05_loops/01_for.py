# Looping Through a Range
# range(start, end, step)
for i in range(1, 11):  # A sequence from 1 to 10
  if i % 2 == 0:
    print(i, " is even")
  else:
    print(i, " is odd")

for i in range(1, 11, 3):  # A sequence from 1 to 10 with a step of 3
  print(i)

# Looping Through a List/String
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print(float_list)

for i in range(0, len(float_list)):  # Iterator traverses to the last index of the list
  float_list[i] = float_list[i] * 2

print(float_list)

# ===========================
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num in float_list:  # Iterator traverses to the last index of the list
  if num > 10:
    count_greater += 1

print(count_greater)
