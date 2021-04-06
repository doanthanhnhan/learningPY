class Rectangle:
  def __init__(self, length, width):
    self.__width = width
    self.__length = length
    pass

  def area(self):
    return self.__width * self.__length
    pass

  def perimeter(self):
    return 2 * (self.__width + self.__length)
    pass
