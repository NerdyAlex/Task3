def per_triangle(l1, l2, l3):
    peri_tri = l1 + l2 + l3
    print(peri_tri)


def per_square(l1):
    peri_square = 4 * l1
    print(peri_square)


def per_rect(l, w):
    peri_rect = 2(l + w)
    print(peri_rect)


def main():
    print("Welcome To My Perimeter Calculator")
    shape = ("square(s)", 'rectangle(r)', 'triangle(t)')
    print(shape)
    p = input("pick one shape: ")


    if p == "s":
        l1 = int(input("l1 = "))


        per_square(l1)

    elif p == "t":
        l1 = int(input("l1 = "))
        l2 = int(input("l2 = "))
        l3 = int(input("l3 = "))


        per_triangle(l1, l2, l3)

    elif p == "r":
        l = int(input("length = "))
        w = int(input("width = "))

        per_rect(l, w)

    else:
        print('Wrong input...')



main()        