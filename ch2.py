import turtle

n = int(input("Введите число "))

color = 0
w = turtle.Screen()
w.bgcolor("lightgreen")
height = w.window_height()  #высота
width = w.window_width()    #длина

alex = turtle.Turtle()
alex.shape("turtle")
# alex.color("white")
alex.speed(0)
alex.penup()
alex.setpos(-199, +199)
alex.setpos(-width//2+20, +height//2-20)
alex.right(90)

while n>0:
    if color % 3 == 0 :
        alex.color("red")
    elif (color-1) % 3  == 0: 
        alex.color("green")
    else: 
        alex.color("blue")
    alex.pendown()
    alex.forward(height-50)
    alex.penup()
    alex.left(90)
    alex.forward(20)
    alex.left(90) 
    alex.forward(height-50)
    alex.left(180)
    color += 1
    n -= 1


w.mainloop()