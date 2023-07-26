username = input("enter 3 names: ")
first_initial = username[0]
second_initial_location = username.find(" ") + 1
second_initial = username[second_initial_location]
third_initial_location = username.rfind(" ") + 1
third_initial = username[third_initial_location]
initials = first_initial + '.' + second_initial + '.' + third_initial
print(initials.upper())