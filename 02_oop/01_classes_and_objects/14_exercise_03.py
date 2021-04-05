"""
Implement a Calculator Class

1. Implement an initializer to initialize the values of num1 and num2.
2. Methods
add(), a method which returns the sum of num1 and num2.
subtract(), a method which returns the subtraction of num1 from num2.
multiply(), a method which returns the product of num1 and num2.
divide(), a method which returns the division of num2 by num1.

* Sample Input
obj = Calculator(10, 94);
obj.add()
obj.subtract()
obj.multiply()
obj.divide()

* Sample Output
104
84
940
9.4
"""


class Calculator:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def add(self):
    return self.num1 + self.num2

  def subtract(self):
    return self.num2 - self.num1

  def multiply(self):
    return self.num1 * self.num2

  def divide(self):
    if not self.num1:
      return 0
    return self.num2 / self.num1


obj = Calculator(10, 94);
print("===== Result =====")
print("Num 1 = {}\nNum 2 = {}".format(obj.num1, obj.num2))
print("Add: {}".format(obj.add()))
print("Subtract: {}".format(obj.subtract()))
print("Multiply: {}".format(obj.multiply()))
print("Divide: {}".format(obj.divide()))
obj.add()
obj.subtract()
obj.multiply()
obj.divide()
