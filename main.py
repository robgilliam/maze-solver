from window import Window
from maze import Maze

win = Window(800, 600)
# Add some cells
maze = Maze(10, 10, 3, 2, 40, 40, win)

# maze[0][0].has_right_wall = False
# maze[1][0].has_left_wall = False

# maze[0][0].has_bottom_wall = False
# maze[0][1].has_top_wall = False

# maze[0][1].has_right_wall = False
# maze[1][1].has_left_wall = False

# maze[1][1].has_bottom_wall = False
# maze[1][2].has_top_wall = False

# maze[1][2].has_left_wall = False
# maze[0][2].has_right_wall = False

# maze[0][2].has_bottom_wall = False

# maze[0][0].draw_move(maze[1][0])
# maze[1][0].draw_move(maze[0][0], undo=True)
# maze[0][0].draw_move(maze[0][1])
# maze[0][1].draw_move(maze[1][1])
# maze[1][1].draw_move(maze[1][2])

win.wait_for_close()
