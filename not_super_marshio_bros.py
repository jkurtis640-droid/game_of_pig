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
SPEED = 5
root = tk.Tk()
root.title("Super Marshio Bros")
canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT, bg="black")
new_platforms = canvas.create_rectangle(0, ground_top , 100+(CELL * 2) , (HEIGHT * 2),  fill="brown")
canvas.pack()


def create_platforms():
    platforms = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1]
    ]

    platforms = [0,0,0,1,0]

    for p in platforms:
        
            if platforms == 1:
                x1, y1, x2, y2 = canvas.create_rectangle(platforms)
                platforms.append(p)


def create_player():
    global x,y,PLAYER_SIZE
    player = canvas.create_rectangle(x, y, x+PLAYER_SIZE, y+PLAYER_SIZE, fill="red")
    
def game_loop():
    
    create_platforms()
    root.after(16, game_loop)

def move_left(event):
    canvas.move(player, -15, 0)
def move_right(event):
    canvas.move(player, 15, 0)

root.bind("<Left>", move_left)
root.bind("<Right>",move_right)
create_platforms()
create_player()
game_loop()
root.mainloop()
    
