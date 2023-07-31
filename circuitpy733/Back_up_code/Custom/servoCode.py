import time
import board
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.GP16, duty_cycle=3 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 90, 90):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(5)
    for angle in range(90, 0, -90): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(1)