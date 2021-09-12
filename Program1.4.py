#1.4. Call each class by creating an object to it.

class Fruit:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def myfunc(abc):
    print("This is a " + abc.name)
    print("Mango is " + abc.color)

p1 = Fruit("Mango", "Yellow")
p1.myfunc()