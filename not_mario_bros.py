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
PLAY_WIDTH = COLS * CELL
PLAY_HEIGHT = ROWS * CELL
enemies = []
game_over_text = None
alive = True
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
canvas = tk.Canvas(root,width=PLAY_WIDTH,height=PLAY_HEIGHT,bg="black")
canvas.pack()

player = canvas.create_rectangle(CELL, (ROWS - 3) * CELL, CELL + PLAYER_SIZE, (ROWS - 3) * CELL + PLAYER_SIZE, fill="red", outline="")


platforms = []
platform_data = [
    (0, ROWS-2, COLS, ROWS),
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

def check_platform_collision(prev_py2):
    global PLAYER_DY, ON_GROUND

    ON_GROUND = False

    px1, py1, px2, py2 = canvas.coords(player)
    
    for plat in platforms:
        x1, y1, x2, y2 = canvas.coords(plat)

        if px2 > x1 and px1 < x2:
           
           if PLAYER_DY > 0 and prev_py2 is not None and prev_py2 <= y1 and py2 >= y1:
               canvas.move(player, 0, y1 - py2)
               PLAYER_DY = 0
               ON_GROUND = True
               break
           
           if py2 > y1 and py2 < y1 + 5:
               canvas.move(player, 0, y1 - py2)
               PLAYER_DY = 0
               ON_GROUND = True
               break
           
def check_enemy_collision():
    global alive

    px1, py1, px2, py2 = canvas.coords(player)
    for e in enemies:
        enemy_id = e["id"]
        ex1, ey1, ex2, ey2 = canvas.coords(enemy_id)
        if px2 > ex1 and px1 < ex2:
            if py2 > ey1 and py1 < ey2:
                alive = False
                game_over_text = canvas.create_text(PLAY_WIDTH // 2, PLAY_HEIGHT // 2, text="GAME OVER", fill = "white", font=("Arial", 40, "bold"))
                break
            

def move_enemies(e):
    for e in enemies:
        enemy_id = e["id"]
        dx = e["dx"]

        canvas.move(enemy_id, dx, 0)

        

def wrap_player():
    x1, y1, x2, y2 = canvas.coords(player)

    if x2 < 0:
        canvas.move(player, PLAY_WIDTH - x2, 0)

    elif x1 > PLAY_WIDTH:
        canvas.move(player, -x1, 0)

def wrap_enemies():
    for e in enemies:
        enemy_id = e["id"]

        x1, y1, x2, y2 = canvas.coords(enemy_id)
        if x2 < 0:
            canvas.move(enemy_id, PLAY_WIDTH - x2,0)

        elif x1 > PLAY_WIDTH:
            canvas.move(enemy_id, -x1, 0)

def restart_game(event=None):
    global player, enemies, platforms
    global PLAYER_DX, PLAYER_DY, ON_GROUND
    global alive, game_over_text

    canvas.delete("all")

    enemies.clear()
    platforms.clear()

    PLAYER_DX = 0
    PLAYER_DY = 0
    ON_GROUND = False

    alive = True

    game_over_text = None

    player_x = CELL
    player_y = (ROWS - 3) * CELL

    player_id = canvas.create_rectangle(player_x, player_y, player_x + PLAYER_SIZE, player_y + PLAYER_SIZE, fill="red",outline="")\
    
    globals()["player"] = player_id

    make_platforms(platform_data)

    enemy = canvas.create_rectangle(10 * CELL, (ROWS - 3) * CELL, 10 * CELL + ENEMY_SIZE, (ROWS - 3) * CELL + ENEMY_SIZE, fill="green",outline="")

    enemies.append({ 
        "id": enemy,
        "dx": 2
    })

root.bind("<r>",restart_game)
def update():
    global PLAYER_DY, PREV_PY2
    x1, x2, y1, y2 = canvas.coords(player)
    PREV_PY2 = y2
    PLAYER_DY += GRAVITY

    canvas.move(player, PLAYER_DX, PLAYER_DY)
     
    check_platform_collision(PREV_PY2)
    wrap_player()
    move_enemies(enemies)
    wrap_enemies()
    check_enemy_collision()
    root.after(40, update)

update()
root.mainloop()
