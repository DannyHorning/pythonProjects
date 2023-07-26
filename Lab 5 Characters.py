string = input("Enter a String ")
x = string[0]
for character in string[1: ]:
    if character == string[0]:
        x += "$"
    else:
        x += character
print (x)