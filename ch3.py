import turtle
alex = turtle.Turtle()
color = 0
w = turtle.Screen()
w.bgcolor("lightgreen")
height = w.window_height()  #высота
width = w.window_width()    #длина
alex.shape("turtle")
alex.color("white")
l=int(input())
c=0
while c<20:
  alex.forward(l)
  alex.left(90)
  alex.forward(l)
  l=l+10
  c=c+1
