from model.vietnamese import VietNamese
from model.korean import Korean
from model.italian import Italian


class ConLai(Italian, Korean):
  def __init__(self):
    self.vnObj = Italian()
    self.krObj = Korean()

  def getIsHandsome(self):
    return (self.vnObj.getIsHandsome() or self.krObj.getIsHandsome())


person = ConLai()

print(person.info())

if person.getIsHandsome():
  print("Ban dep trai!")
else:
  print("Ban xau hoac @.@")
