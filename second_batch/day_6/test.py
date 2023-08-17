# import turtle

# turtle.bgcolor("white")
# turtle.pensize(3)
# turtle.speed(50)


# def curve():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(1)


# def heart():
#     turtle.fillcolor("red")
#     turtle.begin_fill()
#     turtle.left(140)
#     turtle.forward(113)
#     curve()
#     turtle.left(120)
#     curve()
#     turtle.forward(112)
#     turtle.end_fill()


# heart()

# turtle.done()


import turtle

turtle.bgcolor("grey")
turtle.pensize(3)
turtle.speed(4)


def triangle(size):
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)


triangle(200)

turtle.done()
