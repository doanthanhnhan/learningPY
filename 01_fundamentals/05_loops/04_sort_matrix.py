import numpy


class Matrix:
  def __init__(self, n=3, m=3):
    self.matrix = [[0] * n] * m
    self.n = n
    self.m = m

  def display(self):
    count = 0
    for i in range(self.n):
      for j in range(self.m):
        count += 1
        self.matrix[i][j] = count
        print(count, end=" ")
      print()

  def create(self, m):
    matrix = [[0] * n] * m


n = int(input("Nhap vao so nguyen n: "))
m = Matrix(n, n)
m.display()
print(m.matrix)
