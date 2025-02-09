import window

from maze import Maze

win = window.Window(800, 600)

maze = Maze(10, 10, 10, 12, 40, 40, win)

maze.solve()

win.wait_for_close()
