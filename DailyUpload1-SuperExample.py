# An example how Super() works when using classes
# Super initializes a method from a parent or sibling class

class Rectangle:
  def __init__(self, width, length):
    self.width = width
    self.length = length

# Super is used to call the __init__ method from rectangle
class Square(Rectangle):
  def __init__(self, width, length):
    super().__init__(width, length)

    # Notice here we don't have to initialize the variables
    # like rectangle because of the super method

  def area(self):
    return self.width * self.length

  def color(self, colour):
    self.colour = colour


class Cube(Square):
  def __init__(self, width, length, height):
    super().__init__(width, length)
    self.height = height

  def volume(self):
    return self.width * self.length * self.height

  # We can call super to inherit from functions too
  def color(self, colour, tint):
    super().color(colour)
    self.tint = tint


square = Square(9, 2)

cube = Cube(9, 2, 3)

print(square.area())
print(cube.volume())
