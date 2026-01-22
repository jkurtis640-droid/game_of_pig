import random 
DICE = (1,2,3,4,5,6)
def roll_die():
    return random.choice(DICE)

roll_die()
    
def player_turn():
    turn_score = 0
    while True:
        options = input("Do You want to roll or hold ")
        options = options.strip().lower()
        
        if options == "roll":
           roll = roll_die()
           print("You rolled:",roll)

           if roll == 1:
                turn_score = 0
                print("Turn over!")
                break
           else:
                turn_score += roll
                print("Turn score:", turn_score)
        elif options == "hold":
            print("Holding with score:", turn_score)
            break

        else:
            print("Invalid choice")
    
    return turn_score

player_turn()

def play_game():
    players = (("Player 1","Player 2"))
    scores = [0,0]
    current_player = 0
    
        


       