#Write a menu driven python program which performs the following:
#a. Find area of circle
#b. Find area of triangle
#c. Find area of square and rectangle
#d. Find Simple Interest


print("------menu-----")
print("1.Area of Circle")
print("2.Area of Tringle")
print("3.Area of Square and Rectangle")
print("4.Simple Interest")
print("Please enter choice between 1-4")
choice = int(input("Please enter choice="))
if choice==1:
    radius = float(input("Please enter radius="))
    area_circle = 3.14 * radius * radius
    print("The area of the circle :", area_circle)

elif choice==2:
    base = float(input("Please enter base="))
    height = float(input("Please enter height="))
    area_triangle = base * height
    print("The area of the triangle :", area_triangle)

elif choice==3:
    length = float(input("Please enter length="))
    width= float(input("Please enter width="))
    area_rectangle = length * width
    print("The area of the rectangle :", area_rectangle)
    sides = float(input("Please enter sides="))
    area_squre = sides * sides
    print("The area of the square :", area_squre)

elif choice == 4:
    principal = float(input("Please enter principal="))
    rate = float(input("Please enter rate="))
    time = float(input("Please enter time="))
    interest_rate = (principal * rate * time) / 100
    print("The interest rate is:", interest_rate)

else:
    print("Please enter valid choice")
