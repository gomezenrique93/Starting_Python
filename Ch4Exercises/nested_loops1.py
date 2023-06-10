def main():
    BASE_SIZE = 8
    for i in range(BASE_SIZE):
        for j in range(BASE_SIZE):
            print('*', end='')
            BASE_SIZE -= 1
        print()
main()
