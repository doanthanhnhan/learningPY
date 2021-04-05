"""
Square Numbers and Return Their Sum
Implement a constructor to initialize the values of three properties: x, y, and z.
Implement a method, sqSum(), in the Point class which squares x, y, and z and returns their sum.

Sample Properties
1, 3, 5

Sample Method Output
35
"""


class Point:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def sqSum(self):
    return self.x ** 2 + self.y ** 2 + self.z ** 2


test = Point(1, 3, 5)
print("Sum: ", test.sqSum())