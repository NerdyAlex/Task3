import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Demo")
root.geometry('300x150')

def convert():
    m = entryInt.get()
    km = float(m / 1000),'km'
    output_str.set(km)
    


label = ttk.Label(root, text="Meters to kilometers", font="Arial 20 bold",
              )
entryInt = tk.IntVar()
frame = ttk.Frame(root)
entry = ttk.Entry(frame, textvariable=entryInt)
button = ttk.Button(frame, text="Convert", command=convert)

label.pack()
entry.pack(side="left", padx=7)
button.pack(side="left")
frame.pack(padx=3)

output_str = tk.StringVar()
output = ttk.Label(root, text="Output", 
                   font="Arial 24 bold", 
                   textvariable= output_str)

output.pack(padx=3)



root.mainloop()