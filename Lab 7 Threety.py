def threety(x):
    for i in range(1,x):
        if i % 3 == 0 and i % 5 == 0:
            print('threevety')
        elif i % 3 == 0:
            print('threety')
        elif i % 5 == 0:
            print('fivety')
        else:
            print(i)
    

threety(51)