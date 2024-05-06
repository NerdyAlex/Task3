from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('My Game')
root.iconbitmap('c:/Users/user/Task3/Fullstack.py/favicon.ico')

my_img = ImageTk.PhotoImage(Image.open("c:/Users/user/Task3/Fullstack.py/hello.jpg"))
my_label = Label(image=my_img)
my_label.pack()






quit_button = Button(root, text="Exist Program", command=root.quit)
quit_button.pack()


root.mainloop()