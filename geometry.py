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
    def __init__(self, left: int, right: int, top: int, bottom: int, window = None):
        self.top_left: Point = Point(left, top)
        self.bottom_left: Point = Point(left, bottom)
        self.bottom_right: Point = Point(right, bottom)
        self.top_right: Point = Point(right, top)
        self.has_top_wall:bool = True
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_bottom_wall: bool = True
        self.window = window
        self.visited = False

    def draw(self):
        top_color = left_color = bottom_color = right_color = "#d9d9d9"
        if self.has_top_wall:
            top_color = "black"
        if self.has_left_wall:
            left_color = "black"
        if self.has_bottom_wall:
            bottom_color = "black"
        if self.has_right_wall:
            right_color = "black"
        Line(self.top_left, self.top_right).draw(self.window.canvas, top_color)
        Line(self.top_left, self.bottom_left).draw(self.window.canvas, left_color)
        Line(self.bottom_left, self.bottom_right).draw(self.window.canvas, bottom_color)
        Line(self.bottom_right, self.top_right).draw(self.window.canvas, right_color)

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "grey"
        from_center = Point((self.top_left.x + self.bottom_right.x) / 2, 
                            (self.top_left.y + self.bottom_right.y) / 2)
        to_center = Point((to_cell.top_left.x + to_cell.bottom_right.x) / 2,
                          (to_cell.top_left.y + to_cell.bottom_right.y) / 2)
        move = Line(from_center, to_center)
        move.draw(self.window.canvas, color)
