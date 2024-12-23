from geometry import Point, Cell
from window import Window
from time import sleep
import random, math

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self.origin: Point = Point(x1, y1)
        self._cells: list[list[Cell]] = []
        self.rows: int = num_rows
        self.cols: int = num_cols
        self.cell_width: int = cell_size_x
        self.cell_height: int = cell_size_y
        self.window: Window = win
        self._create_cells()
        if seed is not None:
            random.seed(seed)

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
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


        
    def _draw_cell(self, i, j):
        cell: Cell = self._cells[j][i]
        if self.window is not None:
            cell.draw()
            self._animate()
    
    def _animate(self):
        self.window.redraw()
        sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.rows - 1][self.cols - 1].has_bottom_wall = False
        self._draw_cell(self.cols - 1, self.rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[j][i].visited = True
        while True:
            possible_directions = []
            if (j - 1 >= 0
                and not self._cells[j-1][i].visited):
                possible_directions.append((i, j-1))
            if (j + 1 < self.rows
                and not self._cells[j+1][i].visited):
                possible_directions.append((i, j+1))
            if (i - 1 >= 0
                and not self._cells[j][i-1].visited):
                possible_directions.append((i-1, j))
            if (i + 1 < self.cols
                and not self._cells[j][i+1].visited):
                possible_directions.append((i+1, j))
            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            direction = math.floor(random.uniform(0,len(possible_directions)))
            x,y = possible_directions[direction]
            if (x < i):
                self._cells[j][i].has_left_wall = False
                self._cells[y][x].has_right_wall = False
            if (x > i):
                self._cells[j][i].has_right_wall = False
                self._cells[y][x].has_left_wall = False
            if (y < j):
                self._cells[j][i].has_top_wall = False
                self._cells[y][x].has_bottom_wall = False
            if (y > j):
                self._cells[j][i].has_bottom_wall = False
                self._cells[y][x].has_top_wall = False
            self._draw_cell(i, j)
            self._draw_cell(x, y)
            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False


