import turtle

turtle.title("Python Turtle Module to create Polygons")


def polygon(n):
    for i in range(n):
        turtle.forward(100)
        turtle.left(360 / n)


# square = polygon(4)
# pentagon = polygon(5)
# hexagon = polygon(6)
# heptagon = polygon(7)
octagon = polygon(8)
# nonagon = polygon(9)
# decagon = polygon(10)


turtle.done()
