import tkinter as tk
import random as r

##DECLARE SOME CONSTANTS

WIDTH = 400
HEIGHT = WIDTH*.75 
PLAYER_SIZE = 30
ENEMY_SIZE = 20

##BUILD OUR WINDOW
root = tk.Tk()
root.title("Avoid The Blocks!")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

##MAKE THE PLAYER
player = canvas.create_rectangle(180, 250, 180+ PLAYER_SIZE, 250+PLAYER_SIZE, fill="magenta")

##MAKE A LIST TO HOLD ENEMIES
enemies = []


##MAKE AN ALIVE BOOL
alive = True
score = 0
score_text = canvas.create_text(10, 10, anchor="nw",text="Score: 0",fill="white",font=("Arial", 14))
gameover_text = None
spawn_timer = 0
fall_speed = 6

##MOVEMENT FUNCTION

def move_left(event=None):
    canvas.move(player, -20, 0)

def move_right(event=None):
    canvas.move(player, 20, 0)

def move_up(event=None):
    canvas.move(player, 0, -20)

def move_down(event=None):
    canvas.move(player, 0, 20)

def restart(event=None):
    global score, block, alive,
##BAD GUYS
def spawn_enemy():
    x = r.randint(0, WIDTH-ENEMY_SIZE)
    block = canvas.create_rectangle(
    x, 0, x+ENEMY_SIZE, ENEMY_SIZE, fill="cyan")
    enemies.append(block)

def run_game():
    global alive,score
    if not alive:
       canvas.create_text(WIDTH // 2, HEIGHT // 2,text="GAME OVER", fill="white", font=("Arial",24))
       return
    score += 1
    canvas.itemconfig(score_text, text=f"Score: {score}")

    global spawn_timer
    spawn_timer += 1
    if spawn_timer >= 10:
        spawn_enemy()
        spawn_timer = 0

    for block in enemies:
       canvas.move(block, 0, fall_speed)
    
       if canvas.bbox(block) and canvas.bbox(player):
          bx1, by1, bx2, by2 = canvas.bbox(block)
          px1, py1, px2, py2 = canvas.bbox(player)

          if bx1< px2 and bx2 > px1 and by1 < py2 and by2 > py1:
             alive = False

          if canvas.bbox(block)[1] > HEIGHT:
              canvas.delete(block)
              enemies.remove(block)
       after_id = root.after(50, run_game)

def restart(event=None):
    global score, alive, player, block
    canvas.delete_all()
    blocks = []
    alive = True
    player = canvas.create_rectangle(180, 250, 180 + PLAYER_SIZE, 250 + PLAYER_SIZE, fill="lime")

##BIND BUTTONS
root.bind("a",move_left)
root.bind("d",move_right)
root.bind("w",move_up)
root.bind("s",move_down)
root.bind("r",restart)
    
restart_btn = tk.Button(root, text="Restart", command=restart)
restart_btn.pack(pady=6)

root.focus_force()

run_game()

root.mainloop()
