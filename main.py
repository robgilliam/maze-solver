from window import Window
from cell import Cell

win = Window(800, 600)
# Add some cells
maze = [
    #First column
    [
        Cell(win),
        Cell(win),
        Cell(win)
    ],
    #Second column
    [
        Cell(win),
        Cell(win),
        Cell(win)
    ]
]

maze[0][0].has_right_wall = False
maze[1][0].has_left_wall = False

maze[0][0].has_bottom_wall = False
maze[0][1].has_top_wall = False

maze[0][1].has_right_wall = False
maze[1][1].has_left_wall = False

maze[1][1].has_bottom_wall = False
maze[1][2].has_top_wall = False

maze[1][2].has_left_wall = False
maze[0][2].has_right_wall = False

maze[0][2].has_bottom_wall = False

for i in range(2):
    for j in range(3):
        x1 = 10 + 50 * i
        x2 = x1 + 50
        y1 = 10 + 50 * j
        y2 = y1 + 50
        maze[i][j].draw(x1, y1, x2, y2)

maze[0][0].draw_move(maze[1][0])
maze[1][0].draw_move(maze[0][0], undo=True)
maze[0][0].draw_move(maze[0][1])
maze[0][1].draw_move(maze[1][1])
maze[1][1].draw_move(maze[1][2])

win.wait_for_close()
