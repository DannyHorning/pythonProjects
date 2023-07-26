integer = int(input("enter an integer > 1 "))
top_range = integer + 1
count = 0
total  = 0

for sum in range(1, top_range):
    total = total + sum
    count = count + 1
avg = total / count
print (avg)