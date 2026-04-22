import tkinter as tk

WIDTH = 400
HEIGHT = 400
CELL = 16
ROWS = WIDTH / CELL
COLS = HEIGHT / CELL
PLAYER_SIZE = 16
ground_top = HEIGHT - (CELL * 2)
x = WIDTH // 14 - PLAYER_SIZE // 14
y = ground_top - PLAYER_SIZE
dx = 0
dy = 0
root = tk.Tk()
root.title("Super Marshio Bros")
canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT, bg="black")
new_platforms = canvas.create_rectangle(0, ground_top , 100+(CELL * 2) , (HEIGHT * 2),  fill="blue")
canvas.pack()


def create_platforms():
    platforms = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
    ]

    for p in platforms:
        for c in range(0, CELL):
            if platforms == 1:
                x1, y1, x2, y2 = canvas.create_rectangle(platforms)
                platforms.append(p)

def create_player():
    global x, y, dx, dy
    player = canvas.create_rectangle(x, y, x+PLAYER_SIZE, y+PLAYER_SIZE, fill="red")
    
    
def game_loop():
    
    create_platforms()
    create_player()
    root.after(16, game_loop)


game_loop()
root.mainloop()
    
