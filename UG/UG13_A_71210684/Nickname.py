import turtle

#Screen
s = turtle.Screen()
s.bgcolor("black")

#Turtle
t = turtle.Turtle()
t.up()
t.pensize(10)
t.color("white")
t.speed(10)

# Huruf N
t.goto(-200,120)
t.down()
t.right(90)
t.fd(120)
t.bk(120)

t.left(40)
t.fd(150)

t.left(140)
t.fd(120)
t.up()

# Huruf I
t.goto(-60,120)
t.down()
t.right(90)
t.fd(40)
t.bk(20)
t.right(90)
t.fd(120)
t.left(90)
t.fd(20)
t.bk(40)
t.up()

# Huruf C
t.goto(60,0)
t.down()
t.circle(60,-180)
t.up()

# Huruf H
t.goto(100,0)
t.down()
t.right(90)
t.fd(120)
t.bk(60)
t.right(90)
t.fd(60)
t.left(90)
t.fd(60)
t.bk(120)
t.up()

# Huruf o
t.goto(250,120)
t.down()
t.left(90)
t.circle(60,360)
t.up()

# Huruf L
t.goto(350,120)
t.down()
t.left(90)
t.fd(120)
t.left(90)
t.fd(60)
t.up()

#garis atas
t.goto(-200,200)
t.down()
t.forward(610)
t.up()

#garis bawah
t.goto(410,-90)
t.down()
t.forward(-610)

t.hideturtle()

s.exitonclick()
