import turtle


def spiral(count):
    
    n = .1
    
    for count_of_circle in range(count):
        for i in range(360):
            n += .001
            mark.forward(n)
            mark.left(1)


mark = turtle.Turtle()
mark.speed(100)
spiral(10)
