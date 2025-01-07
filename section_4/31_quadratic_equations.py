import math

def determine_quadratic():
    a = int(input("What is a? "))
    b = int(input("What is b? "))
    c = int(input("What is c? "))
    positive_root = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    negative_root = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    print("The root is ", positive_root, negative_root)


if __name__ == "__main__":
    determine_quadratic()