def main():
    
    magic_square = [[4,9,2],
                    [3,5,7],
                    [8,1,6]]
    magic_function(magic_square)

def magic_function(square):
    ROWS = 3
    COLS = 3

    total = 0
    horizontal_value = 0
    diagonal_value = 0
    for r in range(ROWS):
        horizontal_value += square[r]
        for c in range(COLS):
            if r == c:
                diagonal_value += square[r][c]
                # print(diagonal_value)

main()
