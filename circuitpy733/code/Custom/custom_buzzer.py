import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull

btn = digitalio.DigitalInOut(board.GP3)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.DOWN


buzz = DigitalInOut(board.GP11)
buzz.direction = Direction.OUTPUT

while True:
    if btn.value:
        buzz.value = True
        print("On")
      
    else:
        buzz.value = False
        print("Off")


