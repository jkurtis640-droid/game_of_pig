import tkinter as tk

from PIL import Image, ImageTk


WIDTH = 400
HEIGHT = 400
ROWS = 24
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
ON_GROUND = True
JUMP_POWER = -11
PLAYER_DY = 0
platforms = []
prev_py1 = 0
prev_py2 = 0
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
    global platforms
    platform_data = [
        [0, 500, 400, 400],
        [50, 280, 200, 295],
        [200, 220, 300, 235],
        [300, 200, 400, 215],
        #[x1, y1, x2, y2]
    ]

    for coords in platform_data:
         
        p_id = canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill="brown")
        platforms.append(p_id)

    

        
def create_player():
    global x,y,PLAYER_SIZE
    player = canvas.create_rectangle(x, y, x+PLAYER_SIZE, y+PLAYER_SIZE, fill="red")
    
    return player

player = create_player()

def check_ground_collision(player):
    global ON_GROUND,PLAYER_DY
    coords = canvas.coords(player)

   
    
    ## Ground collision code
    if  coords[3] >= ground_top:
       ## adds player to the top of the ground to the bottom of the player
       canvas.move(player, 0, ground_top - coords[3])
       PLAYER_DY = 0
       ON_GROUND = True
    else:
       ON_GROUND = False

def check_platform_collision():
    global ON_GROUND, PLAYER_DY
    p_coords = canvas.coords(player)
    px1, px2, py1, py2 = p_coords[0], p_coords[1], p_coords[2], p_coords[3]
    
    for plat in platforms:
        plat_coords = canvas.coords(plat)
        x1, y1, x2, y2 = plat_coords[0], plat_coords[1], plat_coords[2], plat_coords[3]

        # checks if player is on the platform
        if px2 > x1 and px1 < x2:
            if PLAYER_DY >= 0 and py2 <= y1 and (py2 + PLAYER_DY) >= y1:
                canvas.move(player, 0, y1 - py2)
                PLAYER_DY = 0
                ON_GROUND = True
                return
                
        if py2 > x2 and py1 < x1:
            canvas.move(player, 0, y1 - py2)
            PLAYER_DY = 0
            ON_GROUND = True
            return


def game_loop():
    global PLAYER_DY, player
    PLAYER_DY += GRAVITY
    canvas.move(player, 0, PLAYER_DY)
    check_ground_collision(player)
    check_platform_collision()
    root.after(16, game_loop)

def move_left(event):
    global player
    canvas.move(player, -15, 0)

def move_right(event):
    global player
    canvas.move(player, 15, 0)


def jump(event):
    global ON_GROUND, JUMP_POWER, PLAYER_DY
    if ON_GROUND:
       PLAYER_DY = JUMP_POWER
       ON_GROUND = False
       
root.bind("<Left>",move_left)
root.bind("<Right>",move_right)

root.bind("<Up>",jump)

create_platforms()
## check_ground_collision()
check_platform_collision()
game_loop()

root.mainloop()
    
