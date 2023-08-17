import turtle

# for colour in ["red", "orange", "yellow", "green", "blue", "purple"]:
#     turtle.color(colour, colour)
#     turtle.begin_fill()
#     turtle.circle(150)
#     turtle.end_fill()


# turtle.bgcolor("black")
# turtle.pensize(3)
# turtle.speed(5)

# for colour in ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]:
#     turtle.color(colour)
#     turtle.circle(150)
#     turtle.left(360 / 7)

turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(50)
for _ in range(12):
    for colour in ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]:
        turtle.color(colour)
        turtle.circle(70)
        turtle.left(5)


turtle.done()
