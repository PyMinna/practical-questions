try:

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    dv = a / b
    print(dv)

except ValueError:

    print("Invalid number, try again")

except ZeroDivisionError:

    print("cannot divided by zero")