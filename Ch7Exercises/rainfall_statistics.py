def main():
    TOTAL_MONTHS = 12

    rainfall = [0] * TOTAL_MONTHS

    for i in range(TOTAL_MONTHS):
        print("Enter rainfall for month:", i+1) 
        rainfall[i] = float(input("Enter rainfall: "))


main()
