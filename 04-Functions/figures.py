###
# Draw a square
#

import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")
pen = turtle.Turtle()
pen.speed(5)

def draw_square(length):
    
    for i in range(4):
        pen.forward(length)
        pen.right(90)
    
def draw_trangle(a):
    for i in range(3):
        pen.forward(a)
        pen.right(120)
    
def draw_rectangle(a, b):
    for i in range(4):
        if i%2==0:
            pen.forward(a)
            pen.right(90)
        else:
            pen.forward(b)
            pen.right(90)



draw_square(50)
pen.penup()
pen.goto(-100, 100)
pen.pendown()
draw_rectangle(10,50)
pen.penup()
pen.goto(-350, 0)
pen.pendown()
draw_trangle(100)
pen.penup()
pen.goto(-100, 300)
pen.pendown()
draw_square(200)
pen.penup()
pen.goto(200, 100)
pen.pendown()
draw_trangle(170)
pen.penup()
pen.goto(-200,-150)
pen.pendown()
draw_rectangle(100,50)
