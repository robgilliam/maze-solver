class Line:
    def __init__(self, fm, to):
        self._fm = fm
        self._to = to

    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self._fm.x, self._fm.y, self._to.x, self._to.y, fill=fill_colour, width=2
        )
