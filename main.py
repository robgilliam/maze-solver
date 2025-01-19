from window import Window
from line import Line
from point import Point

win = Window(800, 600)
# Draw a triangle
win.draw_line(Line(Point(10,0), Point(100, 200)), "red")
win.draw_line(Line(Point(100,200), Point(10,200)), "blue")
win.draw_line(Line(Point(10,200), Point(10,0)), "black")
win.wait_for_close()
