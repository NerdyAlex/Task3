#modify the code again
class Notebook():
    def __init__(self):
        self.notes=[]
        
    def create(self, name, content):
        self.notes.append({'name': name, 'content': content})
        print(f"{name} is saved sucussfully")

    def edit(self, name):
        edit_name = input("Which note do you want to edit? ")
        for note in self.notes:
            if note['name'] == edit_name:
                new_content = input(f"Enter new content for {edit_name}: ")
                note['content'] = new_content
                print('Edited successfully')
                return
        print('Note does not exist')


    def listing_note(self):
        print("Listing Note...")
        for note in self.notes:
            print(f"Name: {note['name']}\nContent: {note['content']}")
        if not self.notes:
            print("No note exist")

linkers = Notebook()

def links():
    run = True
    print('Welcome..')
    while run:
        print('Menu\n')
        print('1. Create a note')
        print('2. Edit a note')
        
        print('3. list the note')
        print('4. Quit')
        choose = input("Choose form 1-4: ")
        if choose == "1":
            name = input("Enter the Name of the NoteBook: ")
            content = input(f"{name}\n")
            linkers.create(name, content)

        elif choose == "2":
            linkers.edit(name)

        elif choose == "3":
            linkers.listing_note()
        elif choose == "4":
            break
        else:
            print('Wrong choose')


links()