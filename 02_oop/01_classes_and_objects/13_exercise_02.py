"""
Challenge 2: Calculate the Student's Performance
1. Implement a constructor to initialize the values of four properties: name, phy, chem and, bio.
2. Implement a method, totalObtained, in the Student class that calculates total marks of a student.
* Sample Properties
name = Mark
phy  = 80
chem = 90
bio  = 40

* Sample Method Output
obj1.Total()=210
3. Using the totalObtained method, implement another method, percentage,
in the Student class that calculates the percentage of students marks.
Assume that the total marks of each subject are 100.
So, the combined marks of three subjects are 300.

* Sample Input
phy  = 80
chem = 90
bio  = 40
* Sample Output
70
"""


class Student:
  def __init__(self, name, phy, chem, bio):
    self.name = name
    self.phy = phy
    self.chem = chem
    self.bio = bio

  def totalObtained(self):
    return self.phy + self.chem + self.bio

  def percentage(self):
    return self.totalObtained() / 3


test = Student("Mark", 80, 90, 40)
print("===== Result =====")
print("Total = ", test.totalObtained())
print("Percentage = {:2.0f}".format(test.percentage()))
