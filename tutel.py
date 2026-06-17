import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)
t.shape("classic")
colors = ["red","green","blue","purple"]
n = 1
scale = 1
t.color(colors[0])
for i in range(10**4):
    print(i,end="\r")
    i = 1/scale * i
    if i == 10**n:
        t.color(colors[n%4])
        n += 1
    t.forward(math.sin(i/1))
    t.right(math.log(i+1))
turtle.done()