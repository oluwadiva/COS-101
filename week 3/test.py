first_number = float(input("Eter the first number: "))
second_number = float(input("Enter the second number: "))


if first_number <= 0:
    print(f"{first_number} is not allowed!")
elif second_number <= 0:
    print(f"{second_number} is not allowed!")
else:
    quotient = first_number/ second_number

    print(f"Quotient : {quotient : .2f}")

    
