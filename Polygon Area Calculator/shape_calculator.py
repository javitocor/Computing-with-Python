class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter
  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal
  def get_picture(self):
    if self.width > 50 or self.height > 50 :
      return "Too big for picture."
    picture = ""
    for x in range(self.height):
      for y in range(self.width):
        picture += "*"
      else:
        picture += "\n"
    return picture
  def get_amount_inside(self, shape) :
    num_times = self.get_area()/(shape.get_area())
    return int(num_times)

  def __str__(self):
    return "Rectangle(width={width}, height={height})".format(width=self.width, height=self.height)

class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length
  def set_width(self, width):
    self.width = width
    self.height = width
  def set_height(self, height):
    self.height = height
    self.width = height
  def set_side(self, value):
    self.width = value
    self.height = value
  def __str__(self):
    return "Square(side={length})".format(length=self.width)