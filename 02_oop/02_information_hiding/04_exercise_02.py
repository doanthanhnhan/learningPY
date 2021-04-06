class Student:
  def setName(self, name):
      self.__name = name

  def getName(self):
    return self.__name

  def setRollNumber(self, RollNumber):
    self.__RollNumber = RollNumber

  def getRollNumber(self):
    return self.__RollNumber


demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())
