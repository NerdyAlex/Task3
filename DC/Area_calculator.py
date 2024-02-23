# l = length
# w = width
# b = base
# h = heights

def area_rectan(l, w):

    area = l * w
    print(f"The area of the rectangle is {area}")


def area_square(l, w):

    area = l * w
    print(f"The area of the square is {area}")

def area_tri(b, h):
    area = 0.5 * b * h
    print(f"The area of the triangle is {area}")


def intro():
    print("Welcome To My Area Calcukator")
    shape = ("square"(), 'rectangle', 'triangle')
    print(shape)
    p = input("pick one shape: ")

    
    
    if p == "s":
        l = int(input("Lenght:"))
        w = int(input("Width: "))

        area_square(l, w)

    elif p == "r":
        l = int(input("Lenght:"))
        w = int(input("Width: "))

        area_rectan(l, w)

    elif p == "t":
        b = int(input("Base:"))
        h = int(input("Height: "))

        area_tri(b, h)

    else:
        print("Wrong input")



intro()


