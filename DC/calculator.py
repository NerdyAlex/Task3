class Calculator():
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y   
    
    def divide(self, x, y):
        return x // y  

c = Calculator()

x = int(input('first number: '))
y = int(input('second number: '))
z = input("Enter your sign: ")


if z == "+":
    print(c.add(x, y))

elif z == "-":
    print(c.sub(x, y))

elif z == "*":
    print(c.multiply(x, y))

elif z == "//":
    print(c.divide(x, y))

else:
    print("You enter the wrong sign.")


