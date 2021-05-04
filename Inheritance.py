class Shape():
  def what_am_i(self):
    print("I am a shape")
    
class Rectangle(Shape):
  def __init__(self, w, l):
    self.width = w
    self.length = l
  def calculate_perimeter(self):
    return (self.width*2 + self.length*2)
class Square(Shape):
  def __init__(self, s):
    self.s1 = s
  def calculate_perimeter(self):
    return (self.s1 *4) 

rect = Rectangle(2,3)
squ = Square(4)

rect.what_am_i()
squ.
