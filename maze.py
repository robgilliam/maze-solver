import time

from cell import Cell

class Maze:
    def __init__(
        self,
        x1, y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self._win)] * self._num_rows for _ in range(self._num_cols)]

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell_x1 = self._x1 + i * self._cell_size_x
        cell_y1 = self._y1 + j * self._cell_size_y
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)

    def _break_cell_wall(self, i, j, wall):
        if wall == "left":
            self._cells[i][j].has_left_wall = False

        if wall == "right":
            self._cells[i][j].has_right_wall = False

        if wall == "top":
            self._cells[i][j].has_top_wall = False

        if wall == "bottom":
            self._cells[i][j].has_bottom_wall = False

        self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._break_cell_wall(0, 0, "top")
        self._break_cell_wall(self._num_cols - 1, self._num_rows - 1, "bottom")
