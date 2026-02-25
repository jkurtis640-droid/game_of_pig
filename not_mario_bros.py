import tkinter as tk

WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 30
ENEMY_SIZE = 25
GRAVITY = 0.5
JUMP_POWER = 13
ROWS = 20
COLS = 26
CELL = 30 
MOVE_SPEED = 5
PLAYER_DX = 0
PLAYER_DY = 0
ON_GROUND = False
enemies = []
pattern = [
          "0000011100000000"
          "000001111100000"
          "000111111100000"
          "0000111111100000"               
          "0001111111110000"
          "0011111111111000"
          "0000111111111100"
          "0000011111110000"
          "0000001111100000"
          "0000001111110000"
          "0000011111111100"                           
          "0011111111111110"
          "0111111111111111"
          "1111111111110111"
          "0101111111110010"
          "0011111111111000"
          "0011111111111100"
          "0011110001111000"         
          "0011100000111000"
          "0111100000111100"
           ]                                
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

enemy = canvas.create_rectangle(
    10 * CELL, (ROWS - 3) * CELL, 10 * CELL + ENEMY_SIZE, (ROWS - 3) * CELL + ENEMY_SIZE, fill="green", outline=""

)
    
enemies.append({
    "id": enemy,
    "dx": 2,
})



def jump(event):
    global PLAYER_DY

    if ON_GROUND:
       PLAYER_DY = -JUMP_POWER

def key_press(event):
    global PLAYER_DX

    if event.keysym == "Left":
        PLAYER_DX = -MOVE_SPEED
    elif event.keysym == "Right":
        PLAYER_DX = MOVE_SPEED

def key_release(event):
    global PLAYER_DX

    if event.keysym in ("Left", "Right"):
       PLAYER_DX = 0
root.bind("<KeyPress>",key_press)
root.bind("<KeyRelease>",key_release)
root.bind("<Up>",jump)
make_platforms(platform_data)
def get_player_coords():
    return canvas.coords(player)

def check_platform_collision():
    global PLAYER_DY, ON_GROUND

    ON_GROUND = False

    px1, py1, px2, py2 = canvas.coords(player)
    
    for plat in platforms:
        x1, y1, x2, y2 = canvas.coords(plat)

        if px2 > x1 and px1 < x2:
           
           if py2 >= y1 and py2 <= y1 + PLAYER_DY and PLAYER_DY > 0:
               canvas.move(player, 0, y1 - py2)
               PLAYER_DY = 0
               ON_GROUND = True

def move_enemies(e):
    for e in enemies:
        enemy_id = e["id"]
        dx = e["dx"]

        canvas.move(enemy_id, dx, 0)

        x1, y1, x2, y2 = canvas.coords(enemy_id)

        if x1 <= 0 or x2 >= WIDTH:
            e["dx"] *= -1

def update():
    global PLAYER_DY

    PLAYER_DY += GRAVITY

    canvas.move(player, PLAYER_DX, PLAYER_DY)
     
    check_platform_collision()
    move_enemies(e)
    root.after(40, update)

update()
root.mainloop()
