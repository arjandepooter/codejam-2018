#!/usr/bin/env python
import sys


def number_of_cells(grid, X, Y):
    n = 0
    for x in range(X - 1, X + 2):
        for y in range(Y - 1, Y + 2):
            if (x, y) in grid:
                n += 1

    return n


def determine_cell(grid, X, Y):
    r = (10, 0, 0)
    for x in range(2, X):
        for y in range(2, Y):
            n = number_of_cells(grid, x, y)
            if n == 0:
                return x, y
            if n < r[0]:
                r = (n, x, y)
    return r[1], r[2]


def run(A):
    grid = set()
    if A == 20:
        x, y = 4, 5
    if A == 200:
        x, y = 10, 20

    while True:
        X, Y = determine_cell(grid, x, y)

        print("{x} {y}".format(x=X, y=Y))
        sys.stdout.flush()

        newX, newY = [int(c) for c in input().split(" ")]

        if newX == newY == 0:
            return True

        if newX == newY == -1:
            return False

        grid.add((newX, newY))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        r = run(int(input()))

        if not r:
            sys.exit()
