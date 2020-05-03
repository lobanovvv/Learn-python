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

  def multi_polygon(self, polygons_count, size):

    #Draw figure
    def figure(turn_before_draw, corners, mod_size):
      self.left(turn_before_draw)
      for line in range(corners):
        self.left(360.0 / corners)
        self.forward(size + mod_size)

    #Make indent for draw next figure
    def indent(turn_right):
      self.penup()
      self.right(turn_right)
      self.forward(16)
      self.pendown()

    #Draw cross line for cheking center of all figure
    def check_center():
      self.right(72.5)
      self.backward(280 / 2)
      self.left(90)
      self.color("red")
      self.forward(150)
      self.backward(300)
      self.forward(150)
      self.right(90)
      self.color("black")
      self.backward(280 / 2)
        
    #Triangle
    figure(30, 3, -5)
    indent(30)

    #4-side polygon
    figure(45, 4, 10)
    indent(45)

    #5-side polygon
    figure(55, 5, 20)
    indent(55)

    #6-side polygon
    figure(60, 6, 25)
    indent(60)

    #7-side polygon
    figure(65, 7, 28)
    indent(65)

    #8-side polygon
    figure(67.5, 8, 30)
    indent(67.5)

    #9-side polygon
    figure(70, 9, 31)
    indent(70)

    #10-side polygon
    figure(72.5, 10, 32)


mark = Moves()
mark.speed(5)
mark.shape('turtle')

mark.multi_polygon(polygons_count = 3, size = 55)
#mark.multi_square(22, 22)
#mark.more_square(total_square = 10, size = 10, move_out = 10)
#mark.square(44)
#mark.circle_v2()
#mark.more_square(10,22,22)

