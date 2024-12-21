from window import Window
from geometry import Line, Point



def main():
    win = Window(800, 600)
    lines = []
    lines.append(Line(Point(10, 10), Point(10, 90)))
    lines.append(Line(Point(300, 20), Point(150, 175)))
    lines.append(Line(Point(75, 20), Point(400, 13)))
    for line in lines:
        win.draw_line(line, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()
