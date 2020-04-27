import turtle
from init import *
from numbers import *

w = turtle.Screen()
w.bgcolor(bgcolor)
height = w.window_height()
width = w.window_width()

alex = turtle.Turtle()
alex.shape(names[pos_name])
alex.color(fgcolor)
alex.speed(speed)
alex.pensize(pensize)

change_pos(alex, -width // 2 + 10, +height // 2 - 10)

step = 100

sp = int(turtle.numinput('Вопрос', 'Введите цифру: ', default=2))

if sp == 0: get_zero(alex,step)
elif sp == 1: get_one(alex,step)
elif sp == 2: get_two(alex,step)
elif sp == 3: get_three(alex, step)
elif sp == 4: get_four(alex, step)
elif sp == 5: get_five(alex, step)
elif sp == 6: get_six(alex, step)
elif sp == 7: get_seven(alex, step)
elif sp == 8: get_eight(alex,step)
elif sp == 9: get_nine(alex, step)


w.mainloop()
