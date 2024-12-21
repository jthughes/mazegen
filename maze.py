from geometry import Point, Cell
from window import Window
from time import sleep

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.origin: Point = Point(x1, y1)
        self._cells: list[list[Cell]] = []
        self.rows: int = num_rows
        self.cols: int = num_cols
        self.cell_width: int = cell_size_x
        self.cell_height: int = cell_size_y
        self.window: Window = win
        self._create_cells()

    def _create_cells(self):
        for y in range(self.rows):
            rows = []
            for x in range(self.cols):
                cell = Cell(self.origin.x + self.cell_width * x,
                            self.origin.x + self.cell_width * (x + 1),
                            self.origin.y + self.cell_height * y,
                            self.origin.y + self.cell_height * (y + 1),
                            self.window)
                rows.append(cell)
            self._cells.append(rows)
        
        for y in range(self.rows):
            for x in range(self.cols):
                self._draw_cell(x, y)
        
    def _draw_cell(self, i, j):
        cell: Cell = self._cells[j][i]
        cell.draw()
        self._animate()
    
    def _animate(self):
        self.window.redraw()
        sleep(0.01)
