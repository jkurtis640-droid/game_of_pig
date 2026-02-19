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
    scores = {
        "Player 1": 0,
        "Player 2": 0,
    }
    
    players = ["Player 1", "Player 2"]

    current_index_of_players = 0
    
    while True:
         current_player = players[current_index_of_players]

         print("\n" + current_player + "'s turn")
         print("Total score: " + str(scores[current_player]))

         turn_score = player_turn()

         scores[current_player] = scores[current_player] + turn_score

         if scores[current_player] >= 100:
            print(current_player + " wins with " + str(scores[current_player]) + " points!")
            break
         
         current_index = (current_index + 1) % len(players)

play_game()

def get_player_choice():
    global valid_choices


       