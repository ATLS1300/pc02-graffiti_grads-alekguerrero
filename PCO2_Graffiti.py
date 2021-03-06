#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

t = turtle.Turtle()
t.hideturtle()
leftEye = (-15,108)
leftAntenna = (-55,220)
rightAntenna = (4,221)
leftPupil = (-6,112)
fingertip = (111,-90)
rightPupil = (50,130)
mustacheLeft = (-5,63)
leftEar = (-74,63)
chinLeft = (10,25)

#Left Antenna Martian (Shape 1 & 2)
t.penup()
t.goto(leftAntenna)
t.lt(120)
t.pendown()
t.speed(15)
t.pencolor(76,153,0)
t.fillcolor(0,255,0)
t.pensize(5)
t.fd(100)
t.rt(20)
t.begin_fill()
t.circle(10)
t.end_fill()

#Right Antenna Martian (Shape 1 & 2)
t.penup()
t.goto(rightAntenna)
t.rt(45)
t.pendown()
t.fd(100)
t.rt(20)
t.begin_fill()
t.circle(10)
t.end_fill()

#Left Eye While Loop Circles (Shape 2)
t.penup()
t.goto(leftPupil)
t.lt(55)
t.pendown()
t.pencolor(204,0,0)
t.fillcolor(204,0,0)
t.pensize(2)
n = 5
while n<=15:
    t.circle(n)
    n = n+5

#Right Eye While Loop Circles (Shape 2)
t.penup()
t.goto(rightPupil)
t.lt(55)
t.pendown()
t.pencolor(204,0,0)
t.fillcolor(204,0,0)
t.pensize(2)
n = 5
while n<=15:
    t.circle(n)
    n = n+5

#Fingertip Laser Triangle 1 (Shape 3)
t.penup()
t.goto(fingertip)
t.pendown()
t.lt(180)
t.fillcolor(255,243,0)
t.pencolor(57,255,20)
t.begin_fill()
t.fd(200)
t.lt(70)
t.fd(40)
t.goto(fingertip)
t.end_fill()

#Fingertip laser Triangle 2 (Shape 3)
t.rt(110)
t.begin_fill()
t.fd(220)
t.lt(90)
t.fd(35)
t.goto(fingertip)
t.end_fill()

#Fingertip laser Triangle 2 (Shape 3)
t.rt(10)
t.begin_fill()
t.fd(220)
t.lt(90)
t.fd(35)
t.goto(fingertip)
t.end_fill()

#Mustache (Shape 4)
t.penup()
t.goto(mustacheLeft)
t.rt(180)
t.pendown()
t.fillcolor(0,0,0)
t.pencolor(0,0,0)
t.begin_fill()
t.fd(5)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(5)
t.lt(90)
t.end_fill()
t.goto(mustacheLeft)

#Earring (Shape 5 - Unfilled)
t.penup()
t.goto(leftEar)
t.lt(80)
t.pensize(3)
t.pencolor(255,0,127)
t.fillcolor(255,0,127)
t.pendown()
t.fd(50)
c = t.clone()
c.pendown()
c.pencolor(255,0,127)
c.fillcolor(255,0,127)
c.pensize(1)
t.circle(14)
c.begin_fill()
c.circle(6)
c.end_fill()

#Goatee (Shape 3)
t.penup()
t.goto(chinLeft)
t.pencolor(0,0,0)
t.fillcolor(0,0,0)
t.lt(95)
t.pendown()
t.begin_fill()
t.fd(32)
t.rt(105)
t.fd(47)
t.goto(chinLeft)
t.end_fill()

#Red Moon While Loop Circles (Shape 2)
t.penup()
t.goto(-200,65)
t.rt(230)
t.pencolor(255,51,51)
t.fillcolor(255,51,51)
t.pensize(1.5)
t.pendown()
y = 5
while y<=110:
    t.circle(y)
    y = y+5

#Yellow Moon While Loop Circles (Shape 2)
t.penup()
t.goto(200,65)
t.rt(50)
t.pencolor("yellow")
t.fillcolor("yellow")
t.pensize(1.5)
t.pendown()
y = 5
while y<=100:
    t.circle(y)
    y = y+5


t.penup()
t.goto(280,-105)
t.pensize(1)
t.pencolor(0,0,0)
t.fillcolor(181, 138, 74)
t.pendown()
box = input("Would you like to order a package with immediate shipping? Type yes or no: \n ")
if box == "yes":
     t.begin_fill()
     for b in range(4):
         t.fd(50)
         t.rt(90)
     t.end_fill()
        
     
#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()

