# Class methods are accessed using the class name and can be accessed without creating a class object.
class Player:
  teamName = 'Liverpool'  # class variables

  def __init__(self, name):
    self.name = name  # creating instance variables

  @classmethod
  def getTeamName(cls):
    return cls.teamName


print(Player.getTeamName())
