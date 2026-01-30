import tkinter as tk
is_on = False
def say_hi():
    global is_on
    is_on = not is_on 
    if is_on:
        label.config(text = "YouClicked the Button", bg = "green")
        button.config(text = "Un clickMe!", bg = "red")
    else:
        label.config(text = "You Clicked theButton", bg = "red")
        button.config(text="Unclick Me!",bg = "green")
root = tk.Tk()
root.title("My First Tkinter Project")
root.geometry("400x300")

label = tk.Label(root, text="Hello Tkinter")
label.pack()
button = tk.Button(root, text = "Click Me!", command=say_hi)
button.pack()

root.mainloop()
