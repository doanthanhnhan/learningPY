class Dog():
  def sound(self):
    print("woof woof")

  def soundD(self):
    print("dog dog")


class Cat():
  def sound(self):
    print("meow meow")

  def soundC(self):
    print("cat cat")


class Duck():
  def sound(self):
    print("quack quack")

  def soundDuck(self):
    print("duck duck")


class DogCat(Cat, Dog):
  def __init__(self):
    pass

  def soundDC(self):
    super().sound()
    # super().soundC()


class DogCatDuck(DogCat, Duck):
  def soundDCD(self):
    super().soundD()
    super().soundC()
    super().soundDuck()


dc = DogCat()
print("=== Sound ===")
dc.sound()
print("=== SoundDC ===")
dc.soundDC()
# test.display1()

dcd = DogCatDuck()
print("=== Sound ===")
dcd.sound()
print("=== SoundDCD ===")
dcd.soundDCD()
