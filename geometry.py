from tkinter import Tk, BOTH, Canvas

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
