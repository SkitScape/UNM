# Tony Catalfamo
# 11/25/2020
# This program does holiday stuff.

"""
I pledge that this program represents my own
program code. I received help from no one
in designing and debugging my program.

I spent 3 hours on this....mostly just watching the different snowflakes it makes haha
"""

import random as r
import turtle as t


def placer(distance):  # the distance argument is passed to this method for randomizing placement
    t.goto(0, 0)
    t.right(60)
    t.forward(distance)


def flake(width, length):  # the width and length arguments from the main function are passed to this method
    origin = t.pos()
    t.pen(pencolor="white", pensize=width)
    t.pendown()
    for i in range(6):  # draws 6 segments at 60 degree angles to generate snowflake geometry
        t.forward(length)
        t.goto(origin)
        t.right(60)
    t.penup()


def snowflake():
    t.speed(0)
    t.penup()
    t.bgcolor("blue")
    for iterations in range(20):
        distance = r.randint(0, 350)  # generates a distance for randomizing placement in each iteration
        width = r.randint(2, 15)  # generates a width for the turtle brush size for each iteration
        length = r.randint(10, 150)  # generates a length to create a random geometry to the snowflake
        for i in range(6):
            placer(distance)  # calls the placement function 6 times to go the specified distance
            flake(width, length)  # calls the flake function to create a part of the snowflake 6 times


def happyHolidays():
    t.home()
    t.color("green")
    t.write("HAPPY", align="center", font=('impact', 80, 'bold'))
    t.seth(270)
    t.forward(65)
    t.color("red")
    t.write("HOLIDAYS!", align="center", font=('impact', 50, 'bold'))


snowflake()
happyHolidays()
input()
