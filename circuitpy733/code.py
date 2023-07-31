import time
import board
import digitalio
import pwmio
import neopixel
import simpleio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.GP16, duty_cycle=3 ** 15, frequency=50)

my_servo = servo.Servo(pwm)


numpix = 16  # Number of NeoPixels
pixpin = board.GP20  # Pin where NeoPixels are connected
strip = neopixel.NeoPixel(pixpin, numpix, brightness=1)
color = [254, 2, 255]  # RGB color - teal


sine = [  # These are the pixels in order of animation - 36 pixels in total:
    4, 3, 2, 1, 0, 15, 14, 13, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28,
    36, 35, 34, 33, 32, 47, 46, 45, 44, 52, 53, 54, 55, 56, 57, 58, 59, 60]


# Define pin numbers
BUTTON_PIN = board.GP3
BUZZER_PIN = board.GP11
# SERVO_PIN = board.GP16
LED_PIN = board.GP17
MOTOR_PIN = board.GP19

# Initialize button
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Initialize buzzer
# buzzer = pwmio.PWMOut(BUZZER_PIN, duty_cycle=0)

# Initialize servo
# servo = pwmio.PWMOut(SERVO_PIN, duty_cycle=2 ** 15, frequency=50)

# Initialize LED strip
num_pixels = 110  # Change this to the number of LEDs in your strip
led_strip = neopixel.NeoPixel(LED_PIN, num_pixels, auto_write=False)

# initialise Motor
motor =  digitalio.DigitalInOut(MOTOR_PIN)
motor.direction = digitalio.Direction.OUTPUT




# Function to move the servo
# def move_servo(angle):
#     duty_cycle = int(2 ** 15 + (angle / 180) * (2 ** 15))
#     servo.duty_cycle = duty_cycle
#     time.sleep(0.5)
#     servo.duty_cycle = 0

def motor_on():
    motor.value = True

def motor_off():
  motor.value = False

# Function to turn on the LED strip
def turn_on_led():
    led_strip.fill((254, 2, 255))  # Set the color to red (you can change this)
    led_strip.fill((44, 45, 213))
    led_strip.show()

# Function to turn off the LED strip
def turn_off_led():
    led_strip.fill((0, 0, 0))  # Turn off all LEDs
    led_strip.show()

# def onServo_turn():
#     for angle in range(0, 180, 360):  # 0 - 180 degrees, 5 degrees at a time.
#         my_servo.angle = angle
#         time.sleep(1)
#     for angle in range(360, 0, -180): # 180 - 0 degrees, 5 degrees at a time.
#         my_servo.angle = angle
#         time.sleep(1)
def onServo_turn():
    my_servo.angle = 180
    time.sleep(3)

# def led_ring_on():
#     for i in range(len(sine)):
#     # Set 'head' pixel to color:
#         strip[sine[i]] = color
#     # Erase 'tail,' 8 pixels back:
#     strip[sine[(i + len(sine) - 8) % len(sine)]] = [0, 0, 0]
#     strip.write()  # Refresh LED states
#     time.sleep(0.016)  # 16 millisecond delay


def wheel(pos):
      # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos * 3), int(pos * 3), 0)
    elif pos < 170:
        pos -= 85
        return (0, int(255 - pos * 3), int(pos * 3))
    else:
        pos -= 170
        return (int(pos * 3), 0, int(255 - pos * 3))

# Assuming your NeoPixel ring has 16 pixels
numpix = 16

# Initialize NeoPixel strip here with the appropriate parameters for your hardware
# For example:
# strip = neopixel.NeoPixel(board.D6, numpix, brightness=0.2, auto_write=False)

# Define the pink color
def pink_color():
    # Adjust these RGB values to get the desired shade of pink
    return (254, 2, 255)  # (R, G, B)

def rainbow_cycle(numberOfPixels):
    for j in range(numberOfPixels):
        for index in range(numberOfPixels):
            if index < numberOfPixels:
                strip[index] = pink_color()
            elif index >= numberOfPixels:
                strip[index] = (0, 0, 0)  # Turn off the other pixels
        strip.show()

# Call the rainbow_cycle function with a suitable delay (in seconds) to control the speed
# Function to play a sound on the buzzer
def play_buzzer():
    simpleio.tone(board.GP11, 250, duration=1.0)
    time.sleep(1)
    rainbow_cycle(5)
    simpleio.tone(board.GP11, 250, duration=1.0)
    time.sleep(1)
    rainbow_cycle(10)
    simpleio.tone(board.GP11, 250, duration=1.0)
    time.sleep(1)
    rainbow_cycle(16)
    simpleio.tone(board.GP11, 350, duration=0.5)
    simpleio.tone(board.GP11, 200, duration=0.5)
    rainbow_cycle(1)
    

# Main loop
while True:
    if  button.value:  # Button is tapped (button value is False)
        play_buzzer()
        # move_servo(90)  # Move the servo to the 90-degree position
        turn_on_led()
        # led_ring_on()
        # led_ring_wheel()
        motor_on()
        time.sleep(5)  # Add a small delay to avoid multiple taps in quick succession
        motor_off()
        onServo_turn()
        turn_off_led()