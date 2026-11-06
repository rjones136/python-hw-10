# freqweb.py  --  Homework 10, Problem 5: frequency analysis of a book
# fetched from the Internet (e.g. Project Gutenberg).
# (a) draws the frequency graph, (b) writes the letter counts to a file
#     so results from several books can be combined later.
# The file is written as:  letter  count   (one line per letter)

import ssl
import urllib.request
from graphics import GraphWin, Rectangle, Text, Point, Line


def main():
    url = input("Enter the URL of the text file: ")
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    # Some Windows installs of Python cannot verify the site's
    # security certificate, so the download is refused. This
    # context tells urlopen to skip that check for this download.
    context = ssl._create_unverified_context()
    raw = urllib.request.urlopen(request, context=context).read()
    text = raw.decode("utf-8", errors="ignore")
    text = text.upper()

    # 256 buckets: one for each ordinal value 0-255.
    # Characters with ordinals of 256 or more are skipped.
    counts = [0] * 256
    for ch in text:
        if ord(ch) < 256:
            counts[ord(ch)] += 1

    # Letters A-Z live in buckets 65-90; ratios use the letter total.
    total = sum(counts[ord("A") + i] for i in range(26))
    ratios = [counts[ord("A") + i] / total for i in range(26)]
    top = max(ratios)

    print("Letter  Count  Ratio")
    for i in range(26):
        letter = chr(ord("A") + i)
        print(f"{letter}  {counts[ord(letter)]}  {ratios[i]:.4f}")
    print("Total letters:", total)

    # (b) write the counts to a file for combining with other books.
    outname = input("Enter the file to write the results to: ")
    outfile = open(outname, "w", encoding="utf-8")
    for i in range(26):
        letter = chr(ord("A") + i)
        outfile.write(f"{letter} {counts[ord(letter)]}\n")
    outfile.close()
    print("Results written to", outname)

    # (a) draw the graph (same as Problem 3).
    win = GraphWin("Letter Frequency", 800, 500)
    win.setCoords(0, 0, 100, 100)

    Line(Point(8, 10), Point(8, 90)).draw(win)    # y-axis
    Line(Point(8, 10), Point(96, 10)).draw(win)   # x-axis
    Text(Point(50, 96), "Letter frequency (share of all letters)").draw(win)
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
