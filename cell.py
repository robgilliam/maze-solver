from point import Point
from line import Line

cell_size = 20

class Cell:
    def __init__(self, x, y, win):
        self.__win = win
        self.centre = Point(x * cell_size, y * cell_size)

        self.top_left = self.centre.offset(-1 * cell_size / 2, -1 * cell_size / 2)
        self.top_right = self.centre.offset(+1 * cell_size / 2, -1 * cell_size / 2)
        self.bottom_left = self.centre.offset(-1 * cell_size / 2, +1 * cell_size / 2)
        self.bottom_right = self.centre.offset(+1 * cell_size / 2, +1 * cell_size / 2)

        self.walls = [
            Line(self.top_left, self.top_right),
            Line(self.top_right, self.bottom_right),
            Line(self.bottom_left, self.bottom_right),
            Line(self.top_left, self.bottom_left)
        ]

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
