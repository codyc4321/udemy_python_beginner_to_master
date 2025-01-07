import math

def km_to_miles():
    km = float(input("How many kilometers to miles? "))
    print(round(km * 0.621371), 3)

def area_of_circle():
    radius = float(input("What is the radius of the circle? "))
    area = math.pi * radius * radius
    print("Area is ", area)

if __name__ == "__main__":
    km_to_miles()
    area_of_circle()