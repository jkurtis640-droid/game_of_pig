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
SPEED = 1
GRAVITY = 0.5
ON_GROUND = True
JUMP_POWER = -10
PLAYER_DX = 0
PLAYER_DY = 0
ENEMY_SIZE = 16
PLAY_WIDTH = COLS * CELL
PLAY_HEIGHT = ROWS * CELL
platforms = []
goombas = []
enemies = []
alive = True
lives = 3
prev_py1 = 0
prev_py2 = 0
x_col = 20
y_row = 44
prev_gy2 = 0
lives_text = None
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
    if not p_coords:
        return
        
    px1, py1, px2, py2 = p_coords[0], p_coords[1], p_coords[2], p_coords[3]
    
    for plat in platforms:
        plat_coords = canvas.coords(plat)
        x1, y1, x2, y2 = plat_coords[0], plat_coords[1], plat_coords[2], plat_coords[3]
        
        # Check if player is horizontally overlapping the platform
        if px2 > x1 and px1 < x2:
            # Check if landing from above
            if PLAYER_DY >= 0 and py2 <= y1 and (py2 + PLAYER_DY) >= y1:
                canvas.move(player, 0, y1 - py2)
                PLAYER_DY = 0
                ON_GROUND = True
                return
            
            if py2 > y1 and py2 < y1 + 10:
                canvas.move(player, 0, y1 - py2)
                PLAYER_DY = 0
                ON_GROUND = True
                return
            
            elif PLAYER_DY < 0:
                if prev_py1 >= y2 and py1 <= y2:
                   canvas.move(player, 0, y2 - py1)
                   PLAYER_DY = 0
                   return
                
       
def draw_lives():
    global lives_text
    if lives_text:
        canvas.delete(lives_text)
    lives_text = canvas.create_text(
        60, 20, text=f"Lives: {lives}", fill="white", font=("Times New Roman", 16, "bold")
    )
def create_goomba(x_col, y_row):
    x = x_col * CELL//2
    y = y_row * CELL//2

    goomba = canvas.create_rectangle(
        x, y, x + ENEMY_SIZE, y + ENEMY_SIZE, fill="brown", outline=""
    )

    goombas.append({
        "id": goomba,
        "dx": -2,
        "dy": 0,
    })

def check_goomba_platform_collision():
    for g in goombas:
        g["ON_GROUND"]= False
        goomba_id = g["id"]
        gx1, gy1, gx2, gy2 = canvas.coords(goomba_id)
        prev_gy2 = g.get("prev_py2",gy2)
        if gy2 >= ground_top:
            canvas.move(goomba_id, 0, ground_top - gy2)
            g["dy"] = 0
            g["ON_GROUND"] = True
            continue
        
        for plat in platforms:
            x1, y1, x2, y2 = canvas.coords(plat)
            ## Check Horizontal Overlap
            if gx2 >= x1 and gx1 <= x2:
                ## Checks old bottom was above platform top and new bottom was above platform top.
                if prev_gy2 <= y1 and gy2 >= y1:
                    canvas.move(goomba_id, 0, y1 - gy2)
                    g["dy"] = 0
                    g["ON_GROUND"] = True
                    break

def move_goombas():
    for g in goombas:
        goomba_id = g["id"]
        ## applies gravity 
        g["dy"] += GRAVITY
        canvas.move(goomba_id, g["dx"], g["dy"])
        gx1, gy1, gx2, gy2 = canvas.coords(goomba_id)
        g["prev_gy2"] = gy2

def goomba_collision_with_player():
    global alive, lives, PLAYER_DX, PLAYER_DY

    p_coords = canvas.bbox(player)
    if not p_coords:
        return
    
    px1, py1, px2, py2 = p_coords 
    for g in goombas[:]:
        goomba_id = g["id"]
        g_coords = canvas.bbox(goomba_id)
        if not g_coords:
            continue
 

        gx1, gy1, gx2, gy2 = g_coords
        ## Check if the player and goomba are overlapping
        if px2 > gx1 and px1 < gx2 and py2 > gy1 and py1 < gy2:
            # Check if it is a stomp
            if PLAYER_DY >= 0 and (py2 - gy1) <= 10:
               canvas.delete(goomba_id)
               goombas.remove(g)
               PLAYER_DY = -6
            # Otherwise it took damage from the bottom
            elif lives > 0:
                lives -= 1
                draw_lives()
                if lives > 0:
                    # Reset Position
                    canvas.coords(
                        player,
                        CELL,
                        (ROWS-3) * CELL,
                        CELL + PLAYER_SIZE,
                        (ROWS-3) * CELL + PLAYER_SIZE
                    )
                    PLAYER_DX = 0
                    PLAYER_DY = 0
            else:
                alive = False
                canvas.create_text(
                    PLAY_WIDTH/2,
                    PLAY_HEIGHT/2,
                    text="GAME OVER",
                    fill="white",
                    font=("Times New Roman", 30)
                )
            break

    
def game_loop():
    global PLAYER_DY, player, goomba_id
    PLAYER_DY += GRAVITY
    canvas.move(player, 0, PLAYER_DY)
    check_ground_collision(player)
    check_platform_collision()
    move_goombas()
    check_goomba_platform_collision()  
    goomba_collision_with_player()
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
create_goomba(x_col, y_row) # Create a Goomba once at the start
## check_ground_collision()
check_platform_collision()
game_loop()

root.mainloop()
    
