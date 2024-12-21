from tkinter import Tk, BOTH, Canvas
from geometry import Line, Point

class Window():
    def __init__(self, width: int, height: int):
        self.__root: Tk = Tk()
        self.__root.title("Mazegen")
        self.__root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.__root)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, fill_color)
    
    