shape = ('square', 'triangle')
cal = ('area', 'perimeter')
print(shape)

z = input('what shape you want:  ')
c = input('area or perimeter: ')
l = int(input("your lenght: "))
run = 0
while run == True:
    if z == shape[0] and c == cal[0]:
        print(2 * l)

    elif z == shape[0] and c == cal[1]:
        print(l + l + l + l)

    else:
        print('nothing')