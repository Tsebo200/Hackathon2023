import time
import board
import digitalio
import pwmio
import neopixel
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull




btn = digitalio.DigitalInOut(board.GP3)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.DOWN



buzz = DigitalInOut(board.GP11)
buzz.direction = Direction.OUTPUT

pwm = pwmio.PWMOut(board.GP16, duty_cycle=3 ** 15, frequency=50)

my_servo = servo.Servo(pwm)



# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 110

pixels = neopixel.NeoPixel(board.GP17, num_pixels)
pixels.brightness = 0.5

while True:
    if btn.value:

        print("On")

    for angle in range(0, 90, 90):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(5)
    for angle in range(90, 0, -90): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(1)

        pixels.fill((255, 255, 255))
      
    else:
        buzz.value = False
        print("Off")



