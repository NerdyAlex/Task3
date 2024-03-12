class NotePad:
    def __init__(self):
       self.note = {}

    def create(self):
        name = input(f"Enter The Name Of Your NoteBook : ")
        content = input(f"{name}\n")
        self.note[name] = content

        print(f"noteBook {name} has been saved sucussfully")

    def edit_note(self):
        edit = input("Which note do you wanna edit: ")
        if edit in self.note:
            new_content = input(f"{edit}\n")
            self.note[edit] = new_content
            print("Edited sucussfully")

        else:
            print("Note not found")

    
    def delete(self):
        delete_note = input("Enter note to be Deleted: ")
        if delete_note in self.note:
            self.note.pop(delete_note)
            print("Note deleted sucussfully..")

        else:
            print("Note does not exist")

    def list_note(self):
        if self.note:
            print("List of Note...")
            for name, content in self.note.items():
                print(f"Name: {name} \nContent: {content}")
                print()
        else:
            print("No notes found.")
 

notelink = NotePad()

def links():
    run = True
    print('Welcome..')
    while run:
        print('Menu\n')
        print('1. Create a note\n')
        print('2. Edit a note\n')
        print("3. Delete a note\n")
        print('4. list the note\n')
        print('5. Quit\n')
        choose = input("Choose form 1-5: ")
        if choose == "1":
            notelink.create()
        elif choose == "2":
            notelink.edit_note()
        elif choose == "3":
            notelink.delete()
        elif choose == "4":
            notelink.list_note()
        elif choose == "5":
            break
        else:
            print('Wrong choose')


links()