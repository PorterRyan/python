# area_calculator.py

area_type = input("Enter C for Circle, T for Triangle, or R for Rectangle: ")

if area_type == "C":
    radius = float(input("What is the radius? "))
    pi = 3.14159
    area = pi * radius**2

    print(f"The area of your circle is {area}")
        
elif area_type == "T":
    base = float(input("Enter the base of your triangle: "))
    height = float(input("Enter the height of your triangle: "))

    area = (base * height)/2
    print(f"The area of your triangle is {area}")
        
elif area_type == "R":
    base = float(input("Enter the base of your rectangle: "))
    height = float(input("Enter the height of your rectangle: "))

    area = base * height
    print(f"The area of your rectangle is {area}")
        
    #elif area_type == "exit":
#        break
else:
    print("Incorrect input")
