"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down

## Random library
import random
import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")

print("Players, stand up")
## sample between 10 - 25 - range(10,26)
time.sleep(random.randint(10,25))

## Times Up 
    ## Display image
print("Time's up! Last to sit down wins.")

im.show()


## Write names of the people who sat down
## when one name remain state winner 
