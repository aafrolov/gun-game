import tkinter as tk
from ball import Ball
from gun import Gun
from random import randint, choice
from math import gcd

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 1000
BALL_MIN_RADIUS = 20
BALL_MAX_RADIUS = 40
GUN_SIZE = 40
BULLET_SIZE = 10


class Game_Canvas(tk.Canvas):
    def __init__(self, tk_root, width, height, bg):
        self.balls = []
        self.gun = None
        self.bullets = []
        self.bullets_iter = 0
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

    def add_gun(self, x0, y0, x1, y1, width, color):
        gun_id = self.create_line(x0, y0, x1, y1, width=width, fill=color)
        self.gun = Gun(gun_id, x0, y0, x1, y1, color)

    def gun_up(self):
        self.gun.gun_up()
        self.coords(self.gun.id, self.gun.x0, self.gun.y0, self.gun.x1, self.gun.y1)

    def gun_down(self):
        self.gun.gun_down()
        self.coords(self.gun.id, self.gun.x0, self.gun.y0, self.gun.x1, self.gun.y1)

    def fire(self):
        r = BULLET_SIZE

        ball_id = self.create_oval(self.gun.x1 - r, self.gun.y1 - r, self.gun.x1 + r, self.gun.y1 + r, fill='red')

        if len(self.bullets) > 1000:
            self.bullets[self.bullets_iter] = Ball(ball_id, self.gun.x1, self.gun.y1 - r, r,
                                                   (self.gun.x1 - self.gun.x0) //
                                                   gcd(self.gun.x1 - self.gun.x0, self.gun.y1 - self.gun.y0),
                                                   (self.gun.y1 - self.gun.y0) //
                                                   gcd(self.gun.x1 - self.gun.x0, self.gun.y1 - self.gun.y0), 'red')
            self.bullets_iter += 1
            self.bullets_iter %= 1000
        else:
            self.bullets.append(Ball(ball_id, self.gun.x1, self.gun.y1 - r, r, self.gun.x1 - self.gun.x0,
                                     self.gun.y1 - self.gun.y0, 'red'))
        self.kill_enemies()

    def move_bullets(self):
        for bullet in self.bullets:
            self.move(bullet.id, bullet.x_speed, bullet.y_speed)
            bullet.x += bullet.x_speed
            bullet.y += bullet.y_speed

    def kill_enemies(self):
        for bullet in self.bullets:
            itr = len(self.balls)
            for ball in self.balls[::-1]:
                itr -= 1
                if ball.die_checker(bullet.x, bullet.y):
                    self.delete(ball.id)
                    self.balls.pop(itr)

    def motion(self):
        self.move_balls()
        self.kill_enemies()
        self.move_bullets()
        self._root().after(5, self.motion)


root = tk.Tk()
c = Game_Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='black')
c.focus_set()
c.pack()

for i in range(10):
    c.add_ball(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, randint(BALL_MIN_RADIUS, BALL_MAX_RADIUS + 1),
               randint(-3, 3), randint(-3, 3), choice(['white', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']))

c.add_gun(0, CANVAS_HEIGHT // 2, GUN_SIZE, CANVAS_HEIGHT // 2, width=10, color='green')

root.bind("<KeyPress-Up>", lambda e: c.gun_up())
root.bind("<KeyPress-Down>", lambda e: c.gun_down())
root.bind("<space>", lambda e: c.fire())

c.motion()
root.mainloop()
