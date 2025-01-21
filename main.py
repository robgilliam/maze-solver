from window import Window
from cell import Cell

win = Window(800, 600)
# Add some cells
maze = [
    #First row
    [
        Cell(1, 1, win),
        Cell(2, 1, win)
    ],
    #Second row
    [
        Cell(1, 2, win),
        Cell(2, 2, win)
    ]
]
maze[0][0].add_bottom_exit()
maze[0][0].add_right_exit()
maze[0][1].add_left_exit()
maze[1][0].add_top_exit()
maze[1][0].add_right_exit()
maze[1][1].add_left_exit()
maze[1][1].add_bottom_exit()

for cell in [c for r in maze for c in r]:
    cell.draw()

win.wait_for_close()
