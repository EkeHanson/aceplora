import turtle

def square(size):
    turtle.color("cyan","magenta")
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.end_fill()

def rectangle(height,width):
    turtle.color("red", "purple")
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()

square(60)
turtle.penup()
turtle.forward(100)
turtle.pendown()
rectangle(90,80)

turtle.done()