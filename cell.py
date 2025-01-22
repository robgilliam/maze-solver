from point import Point
from line import Line

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.__win = win

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)

        self.walls = [
            Line(top_left, top_right),
            Line(top_right, bottom_right),
            Line(bottom_left, bottom_right),
            Line(top_left, bottom_left)
        ]

        self.centre = Point((x1 + x2) / 2, (y1 + y2) / 2)

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

    def draw_move(self, to_cell, undo=False):
        self.__win.draw_line(Line(self.centre, to_cell.centre), "gray" if undo else "red")
