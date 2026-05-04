import tkinter as tk

from PIL import Image, ImageTk


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
GRAVITY = 0.5
ON_GROUND = False
MOVE_SPEED = 5
root = tk.Tk()
root.title("Super Marshio Bros")
canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT, bg="black")
new_platforms = canvas.create_rectangle(0, ground_top, 100+(CELL * 19) , (HEIGHT * 2),  fill="brown")
canvas.pack()
original_img = Image.open("pixilart-drawing (1).png")

resized_img = original_img.resize((50,50))

sprite_photo = ImageTk.PhotoImage(resized_img)

sprite_id = canvas.create_image(x, y, image=sprite_photo, anchor="nw")

canvas.sprite_photo = sprite_photo
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
    
    return player

player = create_player()

def check_ground_collision(player):
    #global player
    coords = canvas.coords(player)

    ## Gridmap of player
    x1 = coords[0]
    y1 = coords[1]
    x2 = coords[2]
    y2 = coords[3]
    
    ## Ground collision code
    if  coords[3] >= ground_top:
       ## adds player to the top of the ground to the bottom of the player
       player += (ground_top-y2)
       dy = 0
       coords[3]=0
       on_ground = True
    else:
       on_ground = False
def game_loop():
    global y, player
    y += GRAVITY
    canvas.move(player, 0, dy)
    check_ground_collision(player)
    root.after(16, game_loop)

def move_left(event):
    global player
    canvas.move(player, -15, 0)

def move_right(event):
    global player
    canvas.move(player, 15, 0)

root.bind("<Left>",move_left)
root.bind("<Right>",move_right)
create_platforms()

## check_ground_collision()
game_loop()

root.mainloop()
    
