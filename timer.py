"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down

## Random library
<<<<<<< HEAD
import random
=======

## sample between 10 - 25 - range(10,26)

## Times Up 
    ## Display image

## Write names of the people who sat down
    ## when one name remain state winner 


>>>>>>> a099b2af61003375c6abc31a3310ba7f6237446e
import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")

<<<<<<< HEAD
print("Players, stand up")
## sample between 10 - 25 - range(10,26)
time.sleep(random.randint(10,25))

## Times Up 
    ## Display image
print("Time's up! Last to sit down wins.")
=======
# ask user to enter desired countdown time
set_time = int(input("Please set your timer in seconds: "))

time.sleep(set_time)
>>>>>>> a099b2af61003375c6abc31a3310ba7f6237446e

im.show()


## Write names of the people who sat down
## when one name remain state winner 
