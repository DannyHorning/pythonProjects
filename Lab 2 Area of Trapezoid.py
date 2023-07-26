#Write a program to calculate the area of a trapezoid (a quadrilateral with two sides parallel). 
#To find the area of a trapezoid, multiply the sum of the bases (the parallel sides) by the height (the perpendicular distance between the bases), and then divide by 2.
base_1 = int(input("Enter the First Base Number "))
base_2 = int(input("Enter the Second Base Number"))
trap_area = (base_1 + base_2)/2
print("The area of the trapezoid is ", trap_area)
