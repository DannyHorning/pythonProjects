n = 1
list1 = ["p", "q"]
newlist = []
while n < 6:
    for pq in list1:
        pq += str(n)
        newlist.append(pq)
    n += 1
print(newlist)