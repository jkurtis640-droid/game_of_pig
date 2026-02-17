import tkinter as tk

## PARAMETERS
WIDTH = 600
HEIGHT = 400

def make_enemy_sprite():
    pattern = [
        "00100000100",
        "00010001000",
        "00111111100",
        "01011111010",
        "11111111111",
        "10111111101",
        "10100000101",
        "00011011000",
    ]
    h = len(pattern)
    w = len(pattern[0])

    img = tk.PhotoImage(width=w, height=h)
 
    for y in range(h):
        for x in range(w):
            if pattern [y][x] == 1:
                img.put("white", (x,y))


    return img

root = tk.Tk()
root.title("SPACE INVADERS")
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "black")
canvas.pack()