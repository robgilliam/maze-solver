from window import Window
from cell import Cell

win = Window(800, 600)
# Add some cells
maze = [
    #First row
    [
        Cell(10, 10, 30, 30, win),
        Cell(30, 10, 50, 30, win)
    ],
    #Second row
    [
        Cell(10, 30, 30, 50, win),
        Cell(30, 30, 50, 50, win)
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

maze[0][0].draw_move(maze[0][1])
maze[0][1].draw_move(maze[0][0], undo=True)
maze[0][0].draw_move(maze[1][0])
maze[1][0].draw_move(maze[1][1])

win.wait_for_close()
