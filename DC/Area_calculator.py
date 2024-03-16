# l = length
# w = width
# b = base
# h = heights
import math

class Area():    
    def rectangle(self, l, w):
        area = l * w
        print(f"The area of the rectangle is {area}")

    def square(self, l):
        area = 2 * l
        print(f"The area of the square is {area}")

    def triangle(self, b, h):
        area = 0.5 * b * h
        print(f"The area of the triangle is {area}")
        
    def circle(self):
        r = int(input("Radius: "))
        area = (22/7) * (r * r)
        print(f"The area of the circle is {area}")



area = Area()

def intro():
    print("Welcome To My Area Calculator")
    run = True
    while run:
        shape = ("1. Square", '2. Rectangle', '3. Triangle', "4. Circle", "0. Quit... ")
        print("\n".join(shape))
        p = input("pick one shape: ")
            
    
        if p == "1":
            l = int(input("Lenght: "))
            

            area.square(l)

        elif p == "2":
            l = int(input("Lenght: "))
            w = int(input("Width: "))

            area.rectangle(l, w)

        elif p == "3":
            b = int(input("Base: "))
            h = int(input("Height: "))
            
            area.triangle(b, h)

        elif p == "4":

            area.circle()

        elif p == "0":
            break

        else:
            print("Wrong input")



intro()


