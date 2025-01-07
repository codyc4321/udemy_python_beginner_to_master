def rectangle_area(length, width):
    return length * width

def interactive_rectangle_area():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is ", area)


def interactive_triangle_area():
    length = int(input("Enter the area of the triangle: "))
    width = int(input("Enter the base of the triangle: "))
    area = length * width / 2
    print("The area of the triangle is ", area)

def interactive_trapezoid_area():
    top = int(input("Enter the top of the trapezoid: "))
    base = int(input("Enter the base of the trapezoid: "))
    height = int(input("Enter the height of the trapezoid: "))
    area = (top + base) * height / 2
    print("The area of the trapezoid is ", area)

def interactive_displacement():
    final_velocity = int(input("What is the final velocity? "))
    beginnning_velocity = int(input("What is the beginning velocity? "))
    acceleration = int(input("What was the acceleration? "))
    displacement = (final_velocity**2 - beginnning_velocity**2) / (2 * acceleration)
    print("The displacement of the moving object is ", displacement)

if __name__ == "__main__":
    # interactive_rectangle_area()
    # interactive_triangle_area()
    # interactive_trapezoid_area()
    interactive_displacement()