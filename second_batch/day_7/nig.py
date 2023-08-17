import turtle

pen = turtle.Turtle()


def flag(first_colour, second_colour, third_colour):
    def rectangle(colour):
        for i in range(2):
            pen.begin_fill()
            pen.fillcolor(colour)
            pen.fd(50)
            pen.rt(90)
            pen.fd(100)
            pen.rt(90)
            pen.end_fill()

    pen.pensize(4)
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    pen.left(90)
    pen.forward(400)
    pen.right(90)
    rectangle(first_colour)
    pen.forward(50)
    rectangle(second_colour)
    pen.forward(50)
    rectangle(third_colour)
    pen.forward(50)
    pen.hideturtle()


flag("green", "white", "green")
