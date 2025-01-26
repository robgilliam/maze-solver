from window import Window
from maze import Maze

win = Window(800, 600)
# Add some cells
maze = Maze(10, 10, 10, 12, 40, 40, win)
maze._break_entrance_and_exit()
maze._break_walls_r(0,0)

win.wait_for_close()
