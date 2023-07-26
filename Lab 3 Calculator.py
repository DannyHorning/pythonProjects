number_1 = int(input("Enter a number: "))
sign = input("Write a function: (example add, subtract, multiply, or divide) " )
number_2 = int(input("Enter another number: "))

if sign == "add":
    print(number_1 + number_2)
elif sign == "subtract":
    print (number_1 - number_2)
elif sign == "multiply":
    print (number_1 * number_2)
elif sign == "divide":
    print (number_1/number_2)
else:
    print("error in user input")
