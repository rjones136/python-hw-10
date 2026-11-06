# freqdir.py  --  Homework 10, Problem 4
import os
from graphics import GraphWin, Rectangle, Text, Point, Line


def main():
    folder = input("Enter the name of the folder to analyze: ")

    counts = [0] * 26
    total = 0
    files = 0
    for name in os.listdir(folder):
        if name.endswith(".py"):
            files += 1
            path = os.path.join(folder, name)
            text = open(path, "r", encoding="utf-8", errors="ignore").read()
            text = text.upper()
            for ch in text:
                if "A" <= ch <= "Z":
                    counts[ord(ch) - ord("A")] += 1
                    total += 1

    print(f"Processed {files} Python files.")
    ratios = [c / total for c in counts]
    top = max(ratios)

    print("Letter  Count  Ratio")
    for i in range(26):
        print(f"{chr(ord('A') + i)}  {counts[i]}  {ratios[i]:.4f}")
    print("Total letters:", total)

    # ---- draw the graph (same as Problem 3) ----
    win = GraphWin("Letter Frequency in Python Code", 800, 500)
    win.setCoords(0, 0, 100, 100)

    Line(Point(8, 10), Point(8, 90)).draw(win)    # y-axis
    Line(Point(8, 10), Point(96, 10)).draw(win)   # x-axis
    Text(Point(50, 96), "Letter frequency in Python code").draw(win)
    Text(Point(5, 90), f"{top:.3f}").draw(win)
    Text(Point(5, 10), "0").draw(win)

    bar_width = 88 / 26
    for i in range(26):
        height = 80 * (ratios[i] / top)
        x0 = 8 + i * bar_width + 0.5
        x1 = 8 + (i + 1) * bar_width - 0.5
        bar = Rectangle(Point(x0, 10), Point(x1, 10 + height))
        bar.setFill("steelblue")
        bar.draw(win)
        Text(Point((x0 + x1) / 2, 7), chr(ord("A") + i)).draw(win)

    input("Press <Enter> to close the graph.")
    win.close()


main()
