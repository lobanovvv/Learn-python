import turtle

mark = turtle.Turtle()
mark.speed(11)
mark.shape('turtle')

def circle_v2():
  for i in range(360):
    mark.forward(1)
    mark.left(1)

def circle(diamert):
  mark.circle(diamert)

def square(size):
  for i in range(4):
    mark.forward(size)
    mark.left(90)

def more_square(total_square, size, move_out):
  for iteration in range(total_square):
    square(size)
    mark.penup()
    mark.backward(move_out)
    mark.right(90)
    mark.forward(move_out)
    mark.left(90)
    mark.pendown()
    size += move_out*2
    

more_square(10,22,22)
