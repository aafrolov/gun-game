from math import sqrt


class Ball:
    def __init__(self, ball_id, x, y, r, x_speed, y_speed, color):
        self.id = ball_id
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed

    def die_checker(self, bullet_x, bullet_y):
        return sqrt((bullet_x - self.x)**2 + (bullet_y - self.y)**2) < self.r + 10
