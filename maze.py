import random
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
        win = None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._cells = [[None] * self._num_rows for _ in range(self._num_cols)]

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j] = Cell(self._win)
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
            self._cells[i][j]._has_left_wall = False

        if wall == "right":
            self._cells[i][j]._has_right_wall = False

        if wall == "top":
            self._cells[i][j]._has_top_wall = False

        if wall == "bottom":
            self._cells[i][j]._has_bottom_wall = False

        self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._break_cell_wall(0, 0, "top")
        self._break_cell_wall(self._num_cols - 1, self._num_rows - 1, "bottom")

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cell_list = []
            if i > 0:
                if not self._cells[i - 1][j].visited:
                    cell_list.append(("left", i - 1 , j, "right"))

            if i < self._num_cols - 1:
                if not self._cells[i + 1][j].visited:
                    cell_list.append(("right", i + 1 , j, "left"))

            if j > 0:
                if not self._cells[i][j - 1].visited:
                    cell_list.append(("top", i , j - 1, "bottom"))

            if j < self._num_rows - 1:
                if not self._cells[i][j + 1].visited:
                    cell_list.append(("bottom", i, j + 1, "top"))

            if len(cell_list):
                dir,i1,j1,rev = cell_list[random.randint(0, len(cell_list) - 1)]
                self._break_cell_wall(i, j, dir)
                self._break_cell_wall(i1, j1, rev)
                self._break_walls_r(i1, j1)
            else:
                self._draw_cell(i, j)
                return

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        cell = self._cells[i][j]
        cell.visited = True

        if not cell._has_bottom_wall and j + 1 == self._num_rows:
            return True

        if not cell._has_right_wall:
            next_cell = self._cells[i + 1][j]
            if not next_cell.visited:
                cell.draw_move(next_cell)
                if self._solve_r(i + 1, j):
                    return True
                cell.draw_move(next_cell, True)

        if not cell._has_bottom_wall:
            next_cell = self._cells[i][j + 1]
            if not next_cell.visited:
                cell.draw_move(next_cell)
                if self._solve_r(i, j + 1):
                    return True
                cell.draw_move(next_cell, True)

        if not cell._has_left_wall:
            next_cell = self._cells[i - 1][j]
            if not next_cell.visited:
                cell.draw_move(next_cell)
                if self._solve_r(i - 1, j):
                    return True
                cell.draw_move(next_cell, True)

        if not cell._has_top_wall and j != 0:
            next_cell = self._cells[i][j - 1]
            if not next_cell.visited:
                cell.draw_move(next_cell)
                if self._solve_r(i, j - 1):
                    return True
                cell.draw_move(next_cell, True)

        return False

    def solve(self):
        return self._solve_r(0, 0)
