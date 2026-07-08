try:

    num = int(input("Enter a number: "))
    square = num ** 2
    print(square)

except ValueError:

    print("Invalid,Please try again.")