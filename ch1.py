import turtle

n = int(input("Введите число "))

w = turtle.Screen()
w.bgcolor("lightgreen")
height = w.window_height()  #высота
width = w.window_width()    #длина

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("white")
alex.speed(0)
alex.penup()
alex.setpos(-199, +199)
alex.setpos(-width//2+20, +height//2-20)


while n>0:
    alex.pendown()
    alex.forward(width-50)
    alex.right(90)
    alex.penup()
    alex.forward(20)
    alex.right(90)
    alex.forward(width-50)
    alex.left(180)
    n -= 1

# опускается вниз

w.mainloop()