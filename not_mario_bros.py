import tkinter as tk

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 30
ENEMY_SIZE = 25
GRAVITY = 0.6
JUMP_POWER = 12
ROWS = 20
COLS = 26
CELL = 30 
MOVE_SPEED = 5

root = tk.Tk()
root.title("Mario Bros")
canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="black")
canvas.pack()

player = canvas.create_rectangle(CELL, (ROWS - 3) * CELL, CELL + PLAYER_SIZE, (ROWS - 3) * CELL + PLAYER_SIZE, fill="red", outline="")


platforms = []
platform_data = [
    (0, ROWS-2, WIDTH // CELL + 1, ROWS),
    (3, 13, COLS-3, 14),
    (5, 9, COLS-5, 10),
    (7, 5, COLS-7, 6),
]
def make_platforms(platform_data):
    global platforms
    platforms.clear()

    for c1, r1, c2, r2 in platform_data:
        x1 = c1 * CELL
        y1 = r1 * CELL
        x2 = c2 * CELL
        y2 = r2 * CELL
        plat = canvas.create_rectangle(x1, y1, x2, y2, fill="deepskyblue", outline="")
        platforms.append(plat)

        
    return platforms
    
def move_left(event):
    canvas.move(player, -15, 0)
def move_right(event):
    canvas.move(player, 15, 0)

root.bind("<Left>",move_left)
root.bind("<Right>",move_right)

make_platforms(platform_data)
def update():


    root.after(40, update)

update()
root.mainloop()
