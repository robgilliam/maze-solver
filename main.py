from window import Window
from cell import Cell

win = Window(800, 600)
# Add some cells
cells = [
    Cell(10, 10, win),
    Cell(30, 10, win),
    Cell(10, 30, win),
    Cell(30, 30, win)
]
cells[0].add_bottom_exit()
cells[0].add_right_exit()
cells[1].add_left_exit()
cells[2].add_top_exit()
cells[2].add_right_exit()
cells[3].add_left_exit()
cells[3].add_bottom_exit()

for cell in cells:
    cell.draw()

win.wait_for_close()
