A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def buy_and_sell_once(A):
  max_profit = 0
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[j] - A[i] > max_profit:
          max_profit = A[j] - A[i]
  return max_profit


print(buy_and_sell_once(A))
