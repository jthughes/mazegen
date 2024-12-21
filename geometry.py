from tkinter import Canvas


class Point():
    def __init__(self, x:float, y:float):
        self.x:float = x
        self.y:float = y

class Line():
    def __init__(self, p1: Point, p2: Point):
        self.p1: Point = p1
        self.p2: Point = p2
    
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell():
    def __init__(self, left: int, right: int, top: int, bottom: int, window):
        self.top_left: Point = Point(left, top)
        self.bottom_left: Point = Point(left, bottom)
        self.bottom_right: Point = Point(right, bottom)
        self.top_right: Point = Point(right, top)
        self.has_top_wall:bool = True
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_bottom_wall: bool = True
        self.window = window

    def draw(self):
        if self.has_top_wall:
            Line(self.top_left, self.top_right).draw(self.window.canvas, "black")
        if self.has_left_wall:
            Line(self.top_left, self.bottom_left).draw(self.window.canvas, "black")
        if self.has_bottom_wall:
            Line(self.bottom_left, self.bottom_right).draw(self.window.canvas, "black")
        if self.has_right_wall:
            Line(self.bottom_right, self.top_right).draw(self.window.canvas, "black")