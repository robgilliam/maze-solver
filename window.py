from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.wm_title("Rob's Window")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas()
        self.canvas.pack()

        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_colour):
        line.draw(self.canvas, fill_colour)
