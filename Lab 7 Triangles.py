def triangles(x, y, z):
    if x == z and x == y:
        print("Triangle is equilateral")
    elif x != z and x != y and z != y:
        print("Triangle is scalene")
    else:
        print('Triangle is isosceles')
    
x = int(input("Enter an number: "))
y = int(input("Enter another number: "))
z = int(input('Enter the last number: '))
triangles(x, y, z)
