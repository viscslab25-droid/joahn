import random,math,turtle

t = turtle.Turtle()
turtle.bgcolor("black")
scale = 1
t.speed(0)
t.color("white")
num = 1000
for i in range(num):
    t.forward(math.radians(i)*random.randint(1,10)*scale)
    t.left(math.radians(i))
turtle.done()