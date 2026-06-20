import calculate

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"The area of the rectangle is: {area}")
print(f"the perimeter of the rectangle is: {perimeter}")