# Class methods are accessed using the class name and can be accessed without creating a class object.
class Player:
  teamName = 'Liverpool'  # class variables

  def __init__(self, name):
    self.name = name  # creating instance variables

  def a(self):
    pass

  @classmethod
  def getTeamName(cls):
    cls.a()
    return cls.teamName


print(Player.getTeamName())
