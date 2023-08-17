import turtle
def green_square(size):
    turtle.bgcolor("white")
    turtle.color("green", "green")
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()

def square(size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)

turtle.left(90)
turtle.forward(300)
green_square(100)
turtle.right(180)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
square(100)
turtle.right(90)
turtle.forward(100)
green_square(100)

turtle.done()