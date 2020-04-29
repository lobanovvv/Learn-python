import turtle

class Moves(turtle.Turtle):

  def circle_v2(self):
    for i in range(360):
      self.forward(1)
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


mark = Moves()
mark.speed(11)
mark.shape('turtle')

    
mark.more_square(total_square = 10, size = 10, move_out = 10)
#mark.square(44)
#mark.circle_v2()
#mark.more_square(10,22,22)

