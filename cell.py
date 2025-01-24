from point import Point
from line import Line

class Cell:
    def __init__(self, win = None):
        self._win = win

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self.centre = Point((x1 + x2) // 2, (y1 + y2) // 2)

        if self._win:
            top_left = Point(x1, y1)
            top_right = Point(x2, y1)
            bottom_left = Point(x1, y2)
            bottom_right = Point(x2, y2)

            if self.has_left_wall:
                line = Line(top_left, bottom_left)
                self._win.draw_line(line, "black")

            if self.has_right_wall:
                line = Line(top_right, bottom_right)
                self._win.draw_line(line, "black")

            if self.has_top_wall:
                line = Line(top_left, top_right)
                self._win.draw_line(line, "black")

            if self.has_bottom_wall:
                line = Line(bottom_left, bottom_right)
                self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        if self._win:
            self._win.draw_line(Line(self.centre, to_cell.centre), "gray" if undo else "red")
