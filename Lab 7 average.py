
def average():
    count = 0
    total = 0
    integer = int(input('enter an integer > 1: '))
    top_range = integer + 1
    for sum in range(1, top_range):
        total = total + sum
        count = count + 1
    avg = total / count
    print (avg)

average()