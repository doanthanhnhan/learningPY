class A:
  name="Default"

  def __init__(self, n = None):
    self.name = n
    print(self.name)

  def m(self):
    print("m of A called")


class B(A):
  # def m(self):
  #     print("m of B called")
  pass


class C(A):
  def m(self):
    print("m of C called")


class D(B, C):
  def __init__(self):
    self.objB = B()
    self.objC = C()

  def m(self):
    self.objB.m()

  # def m1(self, name):
  #   self.objB.m()
  #   print(name)

  def m1(self, name=None, number=None):
    self.objB.m()
    print(name, number)


# x = D()
# x.m()
# x.m1("Teo")
# x.m1("Nhan", 20)

a = A("Teo")
print(A.name)
print(a.name)

print(D.mro())

