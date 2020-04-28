import turtle 
from init import *


def get_zero(alex, step):
    alex.pendown()
    for _ in range(2):
        alex.forward(step)
        alex.right(90)
        alex.forward(step*2)
        alex.right(90)
    alex.penup()
    alex.forward(step + 50)

def get_one(alex, step):
    alex.penup()
    alex.right(90)
    alex.forward(step)
    alex.pendown()
    alex.left(135)
    alex.forward(step * 2 ** .5)
    alex.right(135)
    alex.forward(step*2)
    alex.penup()
    alex.right(180)
    alex.forward(step*2)
    alex.right(90)
    alex.forward(50)

def get_two(alex, step):
    alex.pendown()
    alex.forward(step)
    alex.right(90)
    alex.forward(step)
    alex.right(45)
    alex.forward(step * 2 ** .5)
    alex.left(135)
    alex.forward(step)
    alex.penup()
    alex.left(90)
    alex.forward(step*2)
    alex.right(90)
    alex.forward(50)

def get_three(alex, step):
    alex.pendown()
    alex.forward(step)
    alex.right(135)
    alex.forward(step * 2 ** .5)
    alex.left(135)
    alex.forward(step)
    alex.right(135)
    alex.forward(step * 2 ** .5)
    alex.penup()
    alex.left(135)
    alex.forward(step)
    alex.left(90)
    alex.forward(step*2)
    alex.right(90)
    alex.forward(50)

def get_four(alex, step):
    alex.pendown()
    alex.right(90)
    alex.forward(step)
    alex.left(90)
    alex.forward(step)
    alex.right(90)
    alex.forward(step)
    alex.right(180)
    alex.forward(step*2)
    alex.penup()
    alex.right(90)
    alex.forward(50)

def get_five(alex, step):
    alex.pendown()
    alex.forward(step)
    alex.left(180)
    alex.forward(step)
    alex.left(90)
    alex.forward(step)
    alex.left(90)
    alex.forward(step)
    alex.right(90)
    alex.forward(step)
    alex.right(90)
    alex.forward(step)
    alex.penup()
    alex.left(180)
    alex.forward(step)
    alex.left(90)
    alex.forward(step*2)
    alex.right(90)
    alex.forward(50)

def get_six(alex, step):
    alex.penup()
    alex.forward(step)
    alex.pendown()
    alex.right(135)
    alex.forward(step * 2 ** .5)
    alex.left(45)
    alex.forward(step)
    alex.left(90)
    alex.forward(step)
    alex.left(90)
    alex.forward(step)
    alex.left(90)
    alex.forward(step)
    alex.penup()
    alex.left(180)
    alex.forward(step)
    alex.left(90)
    alex.forward(step)
    alex.right(90)
    alex.forward(50)

def get_seven(alex, step): 
    alex.pendown()
    alex.forward(step)
    alex.right(135)
    alex.forward(step * 2 ** .5)
    alex.left(45)
    alex.forward(step)
    alex.penup()
    alex.left(90)
    alex.forward(step)
    alex.left(90)
    alex.forward(step*2)
    alex.right(90)
    alex.forward(50)

def get_eight(alex,step):
    alex.pendown()
    for _ in range(2):
        alex.forward(step)
        alex.right(90)
        alex.forward(step*2)
        alex.right(90)
    alex.right(90)    
    alex.forward(step)
    alex.left(90)
    alex.forward(step)   
    alex.penup()
    alex.left(90)
    alex.forward(step)
    alex.right(90)
    alex.forward(50)

def get_nine(alex, step):
    alex.pendown()
    alex.forward(step)
    alex.right(90)
    alex.forward(step)
    alex.right(90)
    alex.forward(step)
    alex.right(90)
    alex.forward(step)
    alex.penup()
    alex.right(135)
    alex.forward(step * 2 ** .5)
    alex.pendown()
    alex.right(90)
    alex.forward(step * 2 ** .5)
    alex.penup()
    alex.left(180)
    alex.forward(step * 2 ** .5) 
    alex.left(45)
    alex.forward(step)
    alex.right(90)
    alex.forward(50)   


    


  

    

    



