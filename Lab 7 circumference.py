def circleCircumference(radius):
    circumference = 3.14 * radius
    print(circumference)

def circleArea(radius):
    area = 3.14 * radius ** 2
    print(area)

radius = int(input('Enter the radius: '))

circleCircumference(radius)
circleArea(radius)