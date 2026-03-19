import tkinter as tk

WIDTH = 400
HEIGHT = 400
CELL = 16
ROWS = WIDTH / CELL
COLS = HEIGHT / CELL
root = tk.Tk()
root.title("Super Marshio Bros")
canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT, bg="black")
canvas.pack()


def create_platforms():
    platforms = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]

    for p in platforms:
        for c in CELL:
            if platforms == 1:
                x1, y1, x2, y2 = canvas.bbox(platforms)
                platforms = canvas.create_rectangle(100, 100, 132, 132,  fill="brown", )
                platforms.append(p)

def game_loop():
    root.after(16, game_loop)
    
root.mainloop()
    
