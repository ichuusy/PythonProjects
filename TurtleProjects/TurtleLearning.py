from turtle import *

tk = Screen()

pensize(4)
bgcolor("cyan")
color("black")
fillcolor ("red")
begin_fill()
forward(100)
left(45)
forward(100)
left(135)
forward(100)
left(45)
forward(100)
end_fill()
left(135)
fillcolor("purple")
begin_fill()
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()
right(90)
forward(100)
left(45)
fillcolor("blue")
begin_fill()
forward(100)
right(135)
forward(100)
right(45)
forward(100)
end_fill()
hideturtle()
input()

tk.mainloop()