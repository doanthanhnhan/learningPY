class Italian():
  def __init__(self, isHandsome=False):
    self.__isHandsome = isHandsome

  def info(self):
    return "I'm a Italian!"

  def getIsHandsome(self):
    return self.__isHandsome
