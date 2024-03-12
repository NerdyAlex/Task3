class Address():
    def __init__(self):
        self.contant = {}

    def new_contant(self, name):
        email = input("Email Address: ")
        phone = input("Phone: ")

        self.contant[name] = [phone, email]   
        print("New contact has been created")

    def searchs(self, search):
              
        if search in self.contant:
            name_info = self.contant[name]
            print(f"Name: {search}\nPhone: {name_info[0]}\nEmail: {name_info[1]}")
               
        else:
            print(f"{search} does not exist in the book")
    
    def editing(self, edited):
        if edited in self.contant:
            edited == self.contant[name]
            new_email = input("New Email Address: ")
            new_phone = input("New Phone: ")
            self.contant[edited] = [new_phone, new_email]
            print(f"{edited} has been edited.")

        else:
            print(f"{edited} does not exist.")

    def deleting(self, deleted):
        if deleted in self.contant:
            self.contant.pop(deleted)

            print(f"{deleted} has been deleted from Address Book")
        else:
            print(f"{deleted} does not exist..")



address = Address()
print("Welcome To Your Address Book")
run = True
while run:
    print("Meun\n")
    print('1. Create a contact.\n')
    print('2. Search for a contact.\n')
    print("3. Edit a contact.\n")
    print('4. Delete a contact.\n')
    print('5. Quit\n')
    
    choice = input("Enter: ")
    if choice == "1":
        name = input("Name: ")
        address.new_contant(name)

    elif choice == "2":
        search = input("Search: ")
        address.searchs(search)
    
    elif choice == "3":
        edited = input("Enter the NAME of the contact you want to EDIT: ")
        address.editing(edited)
    
    elif choice == "4":
        deleted = input("Enter the NAME of the contact you want to DELETE: ")
        address.deleting(deleted)

    elif choice == "5":
        break

    else:
        print("Wrong input. Choose again...(1, 2, 3, 4 or 5)")