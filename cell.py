from point import Point
from line import Line

class Cell:
    def __init__(self, x, y, win):
        self.corners = [
            Point(x, y),
            Point(x + 20, y),
            Point(x + 20, y + 20),
            Point(x, y + 20)
        ]

        self.__win = win
        self.walls = []
        for i in range(0, 4):
            self.walls.append(Line(self.corners[i], self.corners[(i+1) % 4 ]))


    def add_top_exit(self):
        self.walls[0] = None

    def add_right_exit(self):
        self.walls[1] = None

    def add_bottom_exit(self):
        self.walls[2] = None

    def add_left_exit(self):
        self.walls[3] = None

    def draw(self):
        for wall in self.walls:
            if wall:
                self.__win.draw_line(wall, "black")
