# cipher.py  --  Homework 10, Problem 2: Twisted Path Cipher
# (Supplemental Chapter 9, Problem 3: the message is arranged in a
#  grid and a path through the grid, encoded as a list of tuples,
#  decides the order of the letters. Chapter 9 used a fixed 5x6
#  grid, so the longest message is 30 characters.)
# Reads a grid size and a path (a list of tuples) from a file,
# then uses that path to encipher and decipher a message.
#
# Path file format:
#   first line: rows cols
#   following lines: one (row, col) tuple per line, e.g. (0, 0)
#
# How it works: the message is written into the grid row by row,
# and the ciphertext is the letters read off in path order.
# Deciphering does the reverse: the ciphertext is placed into
# the grid along the path, and the plaintext is read row by row.

import ast


def read_path(fname):
    infile = open(fname, "r")
    rows, cols = [int(x) for x in infile.readline().split()]
    path = []
    for line in infile:
        line = line.strip()
        if line:
            r, c = ast.literal_eval(line)
            path.append((r, c))
    infile.close()
    return rows, cols, path


def encipher(message, rows, cols, path):
    message = message.upper()
    size = rows * cols
    if len(message) > size:
        print(f"Message is too long - this grid holds at most {size} characters.")
        return ""
    message = message.ljust(size, "X")  # pad on the right
    # Fill the grid row by row.
    grid = [[""] * cols for _ in range(rows)]
    i = 0
    for r in range(rows):
        for c in range(cols):
            grid[r][c] = message[i]
            i += 1
    # Read the letters off in path order.
    return "".join(grid[r][c] for (r, c) in path)


def decipher(ciphertext, rows, cols, path):
    ciphertext = ciphertext.upper()
    grid = [[""] * cols for _ in range(rows)]
    for i, (r, c) in enumerate(path):
        grid[r][c] = ciphertext[i]
    # Read the grid row by row.
    return "".join(grid[r][c] for r in range(rows) for c in range(cols))


def main():
    fname = input("Enter the name of the path file: ")
    rows, cols, path = read_path(fname)
    print(f"Grid: {rows} rows x {cols} columns, path length {len(path)}")

    choice = input("Encipher or decipher? (E/D): ").upper()
    if choice == "E":
        message = input("Enter the message to encipher: ")
        print("Ciphertext:", encipher(message, rows, cols, path))
    else:
        ciphertext = input("Enter the message to decipher: ")
        print("Plaintext:", decipher(ciphertext, rows, cols, path))


main()
