from window import Window
from geometry import Line, Point, Cell



def main():
    width = 800
    height = 600
    win = Window(width, height)
    size = 30
    cells = []
    for y in range(1, height // size - 1):
        row = []
        for x in range(1, width // size - 1):
            row.append(Cell(x*size, (x+1)*size, y*size, (y+1)*size, win))
        cells.append(row)

    a = cells[4][5]
    a.has_top_wall = False
    a.has_bottom_wall = False
    b = cells[3][5]
    b.has_top_wall = False
    b.has_bottom_wall = False
    a.draw_move(b)
    

    for row in cells:
        for cell in row:
            cell.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()
