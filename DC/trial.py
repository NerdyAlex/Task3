def notes():
   def note(self):
       self.note = {}

   def create(self):
        self.name = input(f"Enter The Name Of Your NoteBook : ")
        self.content = input(f"{self.name}\n")
        self.note.append(f"name: {self.name},\ncontent: {self.content}")
        print(f"noteBook {self.name} has been saved sucussfully")
    

   def edit(self):
        edit_note = input("Which note do you wanna edit: ")
        if edit_note in self.note:
            new_content = input(f"{edit_note}\n")
            self.content == edit_note
            print("Edited sucussfully")

        else:
            print("Note not found")


z= notes()
print(z)