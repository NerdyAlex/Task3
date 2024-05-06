from tkinter import*

window = Tk()

window.config(background='black')
likes = 0
def like():
    global likes
    
    likes+= 1
    print(likes)

button = Button(window, text="Like This", fg='black', command=like)
button.pack()

window.mainloop()