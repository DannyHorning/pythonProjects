string = input("please enter a string ")
if len(string) > 1:
    print(string[0:2] + string[-2: ])
else:
    print("Empty String")