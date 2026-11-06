# freq.py  --  Homework 10, Problem 3
from graphics import GraphWin, Rectangle, Text, Point, Line


def main():
    fname = input("Enter the name of the text file: ")
    text = open(fname, "r", encoding="utf-8").read()
    text = text.upper()

    # Count only the letters A-Z.
    counts = [0] * 26
    total = 0
    for ch in text:
        if "A" <= ch <= "Z":
            counts[ord(ch) - ord("A")] += 1
            total += 1

    ratios = [c / total for c in counts]
    top = max(ratios)  # bonus: highest ratio = top of the y-axis

    print("Letter  Count  Ratio")
    for i in range(26):
        print(f"{chr(ord('A') + i)}  {counts[i]}  {ratios[i]:.4f}")
    print("Total letters:", total)

    # ---- draw the graph (bars, tallest = max ratio) ----
    win = GraphWin("Letter Frequency", 800, 500)
    win.setCoords(0, 0, 100, 100)

    # axes
    Line(Point(8, 10), Point(8, 90)).draw(win)    # y-axis
    Line(Point(8, 10), Point(96, 10)).draw(win)   # x-axis
    Text(Point(50, 96), "Letter frequency (share of all letters)").draw(win)
    Text(Point(5, 90), f"{top:.3f}").draw(win)     # top of y-axis
    Text(Point(5, 10), "0").draw(win)

    bar_width = 88 / 26
    for i in range(26):
        height = 80 * (ratios[i] / top)  # scale so tallest bar reaches 80
        x0 = 8 + i * bar_width + 0.5
        x1 = 8 + (i + 1) * bar_width - 0.5
        bar = Rectangle(Point(x0, 10), Point(x1, 10 + height))
        bar.setFill("steelblue")
        bar.draw(win)
        Text(Point((x0 + x1) / 2, 7), chr(ord("A") + i)).draw(win)

    input("Press <Enter> to close the graph.")
    win.close()


main()
