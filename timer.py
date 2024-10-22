import time
import random
from PIL import Image

# Open the meme image
im = Image.open("times-up.jpeg")

def nerve_of_steel_game():
    """
    This program is used as an example for MGTC28.
    It simulates a party game where players must sit before the random timer ends.
    The last person to sit wins, and an image is shown when the timer is up.
    """

    # Step 1: Display the start of the game
    print("Players stand!")

    # Step 2: Sleep for a random time between 10 and 25 seconds
    sleep_time = random.randint(10, 25)
    print(f"(Waiting for {sleep_time} seconds... You can sit during this time.)")

    #time.sleep(sleep_time)

    # Step 3: Keep track of players sitting down
    players_sitting = []
    
    # Step 4: Time's up! Display the image and result
    print("\nTime's Up!")
    im.show()  # Show the "Time's Up" image
    
    while True:
        # Ask the user to input the names of players who sat down
        name = input("Enter the name of the player who sat down (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        players_sitting.append(name)


    if len(players_sitting) != 1:
        print(f"Players still standing {players_sitting}.")
        input("press any key to continue playing...")
        nerve_of_steel_game()
    else:
        # The last person to sit down wins
        winner = players_sitting[-1]
        print(f"The last person to sit down was {winner}. {winner} wins!")
        print(f"Players still standing: None (all eliminated).")
        input("press any key to start a new game...")
        nerve_of_steel_game()

# Run the game
input("press any key to start game...")
nerve_of_steel_game()
