from math import sqrt, cos, sin


class Gun:
    def __init__(self, gun_id, x0, y0, x1, y1, color):
        self.id, self.x0, self.y0, self.x1, self.y1, self.color = gun_id, x0, y0, x1, y1, color
        self.size = sqrt((self.x1 - self.x0)**2 + (self.y1 - self.y0)**2)
        self.angle = 0
        print(self.size)

    def gun_up(self):
        self.angle -= 0.1
        self.x1 = self.x0 + self.size * cos(self.angle)
        self.y1 = self.y0 + self.size * sin(self.angle)

    def gun_down(self):
        self.angle += 0.1
        self.x1 = self.x0 + self.size * cos(self.angle)
        self.y1 = self.y0 + self.size * sin(self.angle)
