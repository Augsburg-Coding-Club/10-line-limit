# Samuel Yalew
import turtle
import math
pen = turtle.Turtle()
i = 1
t = 0
r = 0
while i > 0:
    pen.goto(r * math.sin(t),r * math.cos(t))
    t += math.pi / 16
    r += 0.1
