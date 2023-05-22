def main():

    # Prompts the user for kilometers
    kilometers = float(input("Enter the amount of miles that you want to convert: "))

    # Function calls for miles converter
    miles_converter(kilometers)

def miles_converter(kil):
    # Converts kilometers to miles
    miles = kil * 0.6214

    # Prints miles
    print("In miles this is ", format(miles, ".2f"))
main()
