class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def offset(self, delta_x, delta_y):
        return Point(self.x + delta_x, self.y + delta_y)