import tkinter as tk
from ball import Ball
from random import randint, choice

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 800
BALL_MIN_RADIUS = 5
BALL_MAX_RADIUS = 30


class Game_Canvas(tk.Canvas):
    def __init__(self, tk_root, width, height, bg):
        self.balls = []
        super().__init__(tk_root, width=width, height=height, bg=bg)

    def add_ball(self, x, y, r, speed_x, speed_y, color):
        ball_id = self.create_oval(x - r, y - r, x + r, y + r, fill=color)
        self.balls.append(Ball(ball_id, x, y, r, speed_x, speed_y, color))

    def move_balls(self):
        for ball in self.balls:
            if ball.x - ball.r < 0 or ball.x + ball.r > self.winfo_width():
                ball.x_speed = -ball.x_speed
            if ball.y - ball.r < 0 or ball.y + ball.r > self.winfo_height():
                ball.y_speed = -ball.y_speed

            self.move(ball.id, ball.x_speed, ball.y_speed)
            ball.x += ball.x_speed
            ball.y += ball.y_speed

    def motion(self):
        self.move_balls()
        self._root().after(10, self.motion)


root = tk.Tk()
c = Game_Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='black')
c.focus_set()
c.pack()

for i in range(1000):
    c.add_ball(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, randint(BALL_MIN_RADIUS, BALL_MAX_RADIUS + 1),
               randint(-5, 5), randint(-5, 5), choice(['white', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))


c.motion()
root.mainloop()
