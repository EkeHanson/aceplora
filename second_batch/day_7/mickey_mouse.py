import turtle

t = turtle.Turtle()
t.speed(10)

# Draw the head
t.penup()
t.goto(0, -40)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(80)
t.end_fill()

# Draw the left ear
t.penup()
t.goto(-70, 50)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw the right ear
t.penup()
t.goto(70, 50)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw the eyes
t.penup()
t.goto(-25, 30)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(15)
t.end_fill()

t.penup()
t.goto(25, 30)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(15)
t.end_fill()

# Draw the pupils
t.penup()
t.goto(-30, 35)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(7)
t.end_fill()

t.penup()
t.goto(20, 35)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(7)
t.end_fill()

# Draw the nose
t.penup()
t.goto(0, 10)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10)
t.end_fill()

# Draw the mouth
t.penup()
t.goto(-30, -20)
t.pendown()
t.right(45)
t.circle(30, 90)

turtle.done()
