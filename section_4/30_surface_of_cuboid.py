
def surface_area_of_cuboid():
    length = float(input("What is the length of the cuboid? "))
    height = float(input("What is the height of the cuboid? "))
    width = float(input("What is the width of the cuboid? "))
    area = 2 * (length * height + height * width + length * width)
    print("Area is ", area)

if __name__ == "__main__":
    surface_area_of_cuboid()