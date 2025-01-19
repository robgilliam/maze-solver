class Line:
    def __init__(self, fm, to):
        self.fm = fm
        self.to = to

    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.fm.x, self.fm.y, self.to.x, self.to.y, fill=fill_colour, width=2
        )
