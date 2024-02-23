l = []
NAME = input("WELCOME TO YOUR NOTEPAD")

def create(name):
    p = input(f"{name}\n")
    

def save(name):    
    l.append(name)

def edit1():
    name = input("Which note: ")
    if name in l:
        new_content = input(f"{name}\n")
        l.append(new_content)
        l.remove(name)
    else:
        print('Nothing')

def delete():
    print(l)
    d = input('Which note do you want to delete: ')
    if d in l:
        l.remove(d)
        print(l)
    else:
        print("Nothing to delete")



def creating():
    run = True
    while run:
        print('Welcome')
        n = input("1.Create a Note\n2.Edit a note\n3.Delete a note\n4.List Notes\n5.quit\nchoose form (1, 2, 3, 4, 5):")
        

        if n == "1":
            name = input("Enter the name of note: ")
            p = input(f"{name}\n")           
            
            s = input("Do you want to save/(yes or no):  ")
            if s == "yes":
                save(name)
                print(l)

            elif s == "no":
                pass
            else:
                print("Nothing here")

        elif n == "2":
            print(l)

            
            edit1()

        elif n =="3":
            delete()

        elif n == "4":
            print(l)

        elif n == "5":
            break

        else:
            print('Something happen check the code')

    else:
        quit("Stop")



creating()