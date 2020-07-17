from tkinter import *
from ball import Ball


def create_ball():
    x = 10
    y = 10
    r = 5
    ball_id = c.create_oval(x - r, y - r, x + r, y + r)

    return Ball(ball_id, x, y, r, 1, 1)


root = Tk()
c = Canvas(root, width=200, height=200, bg='white')
c.focus_set()
c.pack()

b1 = create_ball()


def motion():
    c.move(b1.id, b1.x_speed, b1.y_speed)
    root.after(10, motion)


motion()

root.mainloop()
