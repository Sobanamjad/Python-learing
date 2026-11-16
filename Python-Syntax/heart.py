import turtle as t
import math as m
import random as r
import time 

# Screen Setup
s = t.Screen()
s.setup(900, 750)
s.bgcolor("black")
s.title("Heart")
s.colormode(1)

t.tracer(0)
t.hideturtle()
t.speed(0)

# heart Setting
SCALE = 16
THREADS = 420
SEGMENTS = 12

# Pink Gradient
def pink_color(f):
    red = 1.0
    green = 0.12 + 0.55 * (1 - f)
    blue = 0.35 + 0.55 * (1 - f)
    return (red, green, blue)

# Heart Drawing 
for i in range(THREADS):

    # Angle around the heart
    a = 2 * m.pi * i / THREADS

    # Methamatical heart outline 
    xo = 16 * (m.sin(a)**3) * SCALE
    yo = (13 * m.cos(a) - 5 * m.cos(2*a) - 2 * m.cos(3*a) - m.cos(4*a)) * SCALE

    #  Random thread length
    l = r.uniform(0.15, 0.58)

    # Inner Endpoint 
    xi = xo * (1 - l)
    yi = yo * (1 - l)

    # Draw each thread in small glowing looking segments
    for j in range(SEGMENTS):
        f = j / SEGMENTS

        x1 = xo + (xi - xo) * f
        y1 = yo + (yi - yo) * f

        x2 = xo + (xi - xo) * (f + 1/SEGMENTS)
        y2 = yo + (yi - yo) * (f + 1/SEGMENTS)

        t.pencolor(pink_color(f))
        t.pensize(r.uniform(0.7, 1.5))

        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)
    
    # Show the Drawing Progressively
    if i % 4 == 0:

        t.update()
        time.sleep(0.008)
    
# Finish
t.update()
t.done()
