from window import Window
from geometry import Line, Point, Cell
from maze import Maze


def main():
    width = 800
    height = 600
    win = Window(width, height)
    size = 30
    maze = Maze(size, size, (height // size) - 2 , (width // size) - 2, size, size, win)
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()
