import turtle
import random

def khangdang():
    t = turtle.Turtle()
    t.speed(10)
    t.color("green")
    t.fillcolor("green")
    t.begin_fill()

    t.right(300)
    t.forward(100)
    t.right(110)
    t.forward(110)
    t.left(50)
    t.backward(120)

    t.forward(60)
    t.right(45)
    t.forward(100)
    t.right(135)
    t.forward(143)
    t.right(137)
    t.forward(105)
    t.end_fill()
    t.right(0)
    t.backward(105)
    t.begin_fill()
    t.right(45)
    t.forward(60)
    t.right(45)
    t.forward(100)
    t.right(135)
    t.forward(143)
    t.right(137)
    t.forward(105)
    t.end_fill()
    t.right(0)
    t.backward(105)

    t.right(42)
    t.forward(65)

    t.fillcolor("brown")
    t.begin_fill()
    t.right(90)
    t.forward(100)
    t.right(270)
    t.forward(40)
    t.right(270)
    t.forward(100)
    t.end_fill()

    return t

turtle.bgcolor("light blue")
tree_position = (0, -310)
snowflakes = []

def draw_text(text, position, font=("Times new roman", 42, "normal")):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("red")
    t.goto(position)
    t.write(text, align="center", font=font)

t = khangdang()
draw_text("Noel này lại một mình rồi  ", tree_position)

for _ in range(100):
    snow = turtle.Turtle()
    snow.shape("circle")
    snow.color("white")
    snow.speed(0)
    snow.penup()
    snow.setx(random.randint(-200, 200))
    snow.sety(random.randint(-200, 200))
    snowflakes.append(snow)

for snow in snowflakes:
    snow.stamp()

t=turtle.mainloop()