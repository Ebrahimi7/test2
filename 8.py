import turtle
from time import sleep
t = turtle.Turtle()

# t.color(1,0.1,0.34)
# t.begin_fill()
# for i in range(40):
#     t.fd(100)
#     t.rt(130)
# t.end_fill()  

def rang(x,y):
    t.speed(0)
    t.color(x)
    for i in range(4):
        t.fd(y)
        t.rt(90)

import random
for n in range(500):
    rang('#FFCA4D',n)