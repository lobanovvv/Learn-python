import turtle

class Moves(turtle.Turtle):

  def circle_v2(self, count):
    n = .1
    for count_of_circle in range(count):
      for i in range(360):
        n += .001
        self.forward(n)
        self.left(1)

  def circle_v1(self, diamert):
    self.circle(diamert)

  def square(self, size):
    for i in range(4):
      self.forward(size)
      self.left(90)

  def more_square(self, total_square, size, move_out):
    for iteration in range(total_square):
      self.square(size)
      self.penup()
      self.backward(move_out)
      self.right(90)
      self.forward(move_out)
      self.left(90)
      self.pendown()
      size += move_out*2

  def multi_square(self, count, length):
    len = length
    for i in range(count):
      self.forward(len)
      self.left(90)
      self.forward(len)
      self.left(90)
      len += length


mark = Moves()
mark.speed(33)
mark.shape('turtle')

mark.multi_square(22, 22)
#mark.more_square(total_square = 10, size = 10, move_out = 10)
#mark.square(44)
#mark.circle_v2()
#mark.more_square(10,22,22)

