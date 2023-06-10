# This program assigns random numbers to 
# a two dimensional list.
import random


def main():
    ROWS = 3
    COLS = 4

    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1,100)

    print(values)
main()

