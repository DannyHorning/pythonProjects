number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))

if number_2 % number_1 == 0:
    print (number_1, "is a multiple of", number_2)
else:
    print (number_1, "is not a multiple of", number_2)