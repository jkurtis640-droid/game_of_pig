import tkinter as tk

# --- Constants ---
WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 30
ENEMY_SIZE = 25
GRAVITY = 0.5
JUMP_POWER = 15
ROWS = 20
COLS = 26
CELL = 30
MOVE_SPEED = 5
dx = 0
dy = 0
# --- Global Variables ---
PLAYER_DX = 0
PLAYER_DY = 0
ON_GROUND = False
PLAY_WIDTH = COLS * CELL
PLAY_HEIGHT = ROWS * CELL
enemies = []
game_over_text = None
alive = True
lives = 3
lives_text = None
player = None
platforms = []
PREV_PY1 = 0
PREV_PY2 = 0
flipped = False
enemy_dx = 0
enemy_dy = 0


platform_data = [
    (0, ROWS-2, COLS, ROWS),
    (2, 16, COLS-2, 17),
    (7, 13, COLS-7, 14),
    (2, 10, COLS-2, 11),
    (7, 7, COLS-7, 8),
    (2, 4, COLS-2, 5)
]

root = tk.Tk()
root.title("Mario Bros")
canvas = tk.Canvas(root, width=PLAY_WIDTH, height=PLAY_HEIGHT, bg="black")
canvas.pack()

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

def jump(event):
    global PLAYER_DY, ON_GROUND
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

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)
root.bind("<Up>", jump)



def flip_enemies_on_platform(plat):
    global flipped, enemy_dx
    x1, y1, x2, y2 = canvas.bbox(plat)
    
    for e in enemies:
        enemy_id = e["id"]
        ex1, ey1, ex2, ey2 = canvas.bbox(enemy_id)

        if ex2 > x1 and ex1 < x2:
            if ey2 >= y1 + CELL and ey2 <= y1 - CELL:
                flipped = True 
                enemy_dx *= -1 
                canvas.itemconfig(enemy_id, fill="orange")
                

def check_platform_collision(prev_py1,prev_py2):
    global PLAYER_DY, ON_GROUND
    ON_GROUND = False
    for plat in platforms:
        coords = canvas.bbox(player)
        if len(coords) != 4:
            continue
    
    px1, py1, px2, py2 = coords

    for plat in platforms:
        x1, y1, x2, y2 = canvas.bbox(plat)

        if px2 > x1 and px1 < x2:

            if PLAYER_DY > 0:
                if prev_py2 <= y1 and py2 >= y1:
                    canvas.move(player, 0, y1 - py2)
                    PLAYER_DY = 0
                    ON_GROUND = True
                    break


                if py2 > y1 and py2 < y1 + 10:
                    canvas.move(player, 0, y1 - py2)
                    PLAYER_DY = 0
                    ON_GROUND = True
                    break

            elif PLAYER_DY < 0:
                 if prev_py1 >= y2 and py1 <= y2:
                    canvas.move(player, 0, y2 - py1)
                    PLAYER_DY = 0
                    break

"""
def check_enemy_collision():
    coords = canvas.bbox(enemies)
    global alive, lives, PLAYER_DX, PLAYER_DY, player, flipped
    
    p_coords = canvas.bbox(player)
    if not p_coords: return
    px1, py1, px2, py2 = p_coords
    
    for e in enemies[:]:
        if flipped == True:
            continue

        if len(coords) != 4:
            continue
        enemy_id = e
        ex1, ey1, ex2, ey2 = canvas.bbox(enemy_id)
        
        if px2 > ex1 and px1 < ex2 and py2 > ey1 and py1 < ey2:
            lives -= 1
            draw_lives()
            if lives > 0:
                # Reset player position
                canvas.bbox(player, CELL, (ROWS - 3) * CELL, CELL + PLAYER_SIZE, (ROWS - 3) * CELL + PLAYER_SIZE)
                PLAYER_DX = 0
                PLAYER_DY = 0
            else:
                alive = False
                canvas.create_text(PLAY_WIDTH/2, PLAY_HEIGHT/2, text="GAME OVER", fill="white", font=("Arial", 30))
            break
"""
def check_enemy_collision():
    global alive, lives, PLAYER_DX, PLAYER_DY, flipped
    
    p_coords = canvas.bbox(player)
    if not p_coords:
        return

    px1, py1, px2, py2 = p_coords

    for e in enemies:
        if e["flipped"]:
            continue

        enemy_id = e["id"]
        coords = canvas.bbox(enemy_id)
        if not coords:
            continue

        ex1, ey1, ex2, ey2 = coords

        if px2 > ex1 and px1 < ex2 and py2 > ey1 and py1 < ey2:
            lives -= 1
            draw_lives()

            if lives > 0:
                canvas.coords(
                    player,
                    CELL,
                    (ROWS - 3) * CELL,
                    CELL + PLAYER_SIZE,
                    (ROWS - 3) * CELL + PLAYER_SIZE
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
                    font=("Arial", 30)
                )
            break
"""
def check_enemy_platform_collision():
    for e in enemies:
         enemy_id = enemies[e]
         ex1, ey1, ex2, ey2 = canvas.bbox(enemy_id)

         for plat in platforms:
             x1, y1, x2, y2 = canvas.bbox(plat)

             if ex2 > x1 and ex1 < x2:
                 if ey2 >= y1 and ey2 <= y1 + 10 and enemy_dy >= 0:
                    canvas.move(enemy_id, 0, y1 - ey2)
                    enemy_dy = 0
                    break
"""
def check_enemy_platform_collision():
    for e in enemies:
        enemy_id = e["id"]
        ex1, ey1, ex2, ey2 = canvas.bbox(enemy_id)

        for plat in platforms:
            x1, y1, x2, y2 = canvas.bbox(plat)

            if ex2 > x1 and ex1 < x2:
                if ey2 >= y1 and ey2 <= y1 + 10 and e["dy"] >= 0:
                    canvas.move(enemy_id, 0, y1 - ey2)
                    e["dy"] = 0
                    break
def move_enemies():
    global dx, dy
    for e in enemies:
        if e["flipped"]:
            continue

        e["dy"] += GRAVITY
        canvas.move(e["id"], e["dx"], e["dy"])

def wrap_player():
    x1, y1, x2, y2 = canvas.bbox(player)
    if x2 < 0:
        canvas.move(player, PLAY_WIDTH, 0)
    elif x1 > PLAY_WIDTH:
        canvas.move(player, -PLAY_WIDTH, 0)


def draw_lives():
    global lives_text
    if lives_text:
        canvas.delete(lives_text)
    lives_text = canvas.create_text(
        60, 20, text=f"Lives: {lives}", fill="white", font=("Arial", 16, "bold")
    )

def spawn_shellcreeper(x_col, y_row):
    x = x_col * CELL
    y = y_row * CELL

    enemy = canvas.create_rectangle(
        x, y, x + ENEMY_SIZE, y + ENEMY_SIZE, fill="green", outline=""
    )
    enemies.append({
        "id": enemy,
        "dx": 2,
        "dy": 0,
        "flipped": False
    })
def wrap_enemies():
    for e in enemies:
        enemy_id = e["id"]
        coords = canvas.bbox(enemy_id)
        if not coords:
            continue

        x1, y1, x2, y2 = coords

        if x2 < 0:
            canvas.move(enemy_id, PLAY_WIDTH + ENEMY_SIZE, 0)
        elif x1 > PLAY_WIDTH:
            canvas.move(enemy_id, -PLAY_WIDTH - ENEMY_SIZE, 0)
            #canvas.move(enemies, -PLAY_WIDTH - ENEMY_SIZE, 0)

def restart_game(event=None):
    global player, enemies, platforms, lives
    global PLAYER_DX, PLAYER_DY, ON_GROUND, alive, lives_text
    
    canvas.delete("all")
    enemies.clear()
    platforms.clear()
    
    PLAYER_DX = 0
    PLAYER_DY = 0
    ON_GROUND = False
    alive = True
    lives = 3
    
    player = canvas.create_rectangle(CELL, (ROWS - 3) * CELL, CELL + PLAYER_SIZE, (ROWS - 3) * CELL + PLAYER_SIZE, fill="red", outline="")
    
    make_platforms(platform_data)
    spawn_shellcreeper(8, 1)
    spawn_shellcreeper(3, 12)
    draw_lives()


def update():
    global PLAYER_DY, PREV_PY1, PREV_PY2
    
    if not alive:
        return

    coords = canvas.bbox(player)
    if not coords: return
    
    x1, y1, x2, y2 = coords
    PREV_PY1 = y1
    PREV_PY2 = y2
    
    PLAYER_DY += GRAVITY
    canvas.move(player, PLAYER_DX, PLAYER_DY)
    
    check_platform_collision(PREV_PY1,PREV_PY2)
    wrap_player()
    move_enemies()
    wrap_enemies()
    check_enemy_collision()
    check_enemy_platform_collision()
    for plat in platforms:
        flip_enemies_on_platform(plat)
    root.after(30, update)

# Initialize
restart_game()
update()
root.mainloop()