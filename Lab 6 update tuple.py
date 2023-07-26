list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
tuple_changed = []
for x in list1:
    newlist = list(x)
    newlist[-1] = 100
    newtuple = tuple(newlist)
    tuple_changed.append(newtuple)
print(tuple_changed)