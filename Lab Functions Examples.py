def add(x, y):
    return x + y
sum = add(1, 1)
print(sum)

sum = lambda x, y : x + y

print(sum(5, 6))

def print_list_items(listToPrint):
    for item in listToPrint:
        print(item)

food = ['pizza', 'sushi', 'hamburger', 'chicken']
fruit = ['apple', 'pear', 'oranges', 'pineapple']

print_list_items(food)
print_list_items(fruit)