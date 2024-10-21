# Timer
### a MGTC28 Python example
This is a timer program written in Python  

![times-up!](https://media.makeameme.org/created/times-up-5923e0.jpg)\
timer.py is a simple Python script allowing users to set timer duration.
Upon timer expiry, the user will see the time-up meme.
timer.py uses the **time library** to help keep track of time and the **pillow library** to facilitate the meme display.

Please see the documentation for the library used:
- [time](https://docs.python.org/3/library/time.html)
- [pillow](https://pypi.org/project/Pillow/)
pseudocode:
START

    DISPLAY "Players stand!"

    // Step 1: Choose a random sleep time between 10 and 25 seconds
    SET sleep_time to a random value between 10 and 25

    DISPLAY "(Waiting for sleep_time seconds... You can sit during this time.)"
    
    // Step 2: Program waits for sleep_time seconds
    WAIT for sleep_time seconds

    // Step 3: Initialize an empty list to keep track of players who sat down
    CREATE an empty list called players_sitting

    // Step 4: Record names of players sitting down
    WHILE True
        PROMPT "Enter the name of the player who sat down (or 'done' to finish): "
        STORE the input in name
        
        IF name equals 'done'
            EXIT the loop
        
        ADD name to players_sitting list

    // Step 5: After sleep time, display "Time's Up" and the image
    DISPLAY "Time's Up!"
    
    SHOW "times-up.jpeg" image

    // Step 6: Determine the winner
    IF players_sitting is empty
        DISPLAY "No players sat down. Everyone is eliminated!"
    ELSE
        SET winner to the last name in players_sitting list
        DISPLAY "The last person to sit down was winner. winner wins!"
        DISPLAY "Players still standing: None (all eliminated)."

END
