"""
A brute-force approach that takes O(n^2)O(n​2)
time to solve with O(1)O(1) space where we loop through the array and create all possible pairings of elements.
"""
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def two_sum_brute_force(A, target):
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[i] + A[j] == target:
        print(A[i], A[j])
        return True
  return False


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum_brute_force(A, target))
target = 20
print(two_sum_brute_force(A, target))
