# l = length
# w = width
# b = base
# h = heights
class Area():    
    def rectangle(l, w):
        area = l * w
        print(f"The area of the rectangle is {area}")

    def square(l, w):
        area = l * w
        print(f"The area of the square is {area}")

    def triangle(b, h):
        area = 0.5 * b * h
        print(f"The area of the triangle is {area}")
        
    def 


area = Area()

def intro():
    print("Welcome To My Area Calculator")
    run = True
    while run:
        shape = ("square (s)", 'rectangle (r)', 'triangle (t)', "1. Quit... ")
        print("\n".join(shape))
        p = input("pick one shape: ")
            
    
        if p == "s":
            l = int(input("Lenght:"))
            w = int(input("Width: "))

            area.square(l, w)

        elif p == "r":
            l = int(input("Lenght:"))
            w = int(input("Width: "))

            area.rectangle(l, w)

        elif p == "t":
            b = int(input("Base:"))
            h = int(input("Height: "))
            area.triangle(b, h)

        elif p == "1":
            break

        else:
            print("Wrong input")



intro()


