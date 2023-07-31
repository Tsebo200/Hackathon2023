import time
import board
import digitalio
import pwmio
import neopixel

# Define pin numbers
BUTTON_PIN = board.GP3
BUZZER_PIN = board.GP11
SERVO_PIN = board.GP16
LED_PIN = board.GP17

# Initialize button
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# Initialize buzzer
buzzer = pwmio.PWMOut(BUZZER_PIN, duty_cycle=0)

# Initialize servo
servo = pwmio.PWMOut(SERVO_PIN, duty_cycle=2 ** 15, frequency=50)

# Initialize LED strip
num_pixels = 110  # Change this to the number of LEDs in your strip
led_strip = neopixel.NeoPixel(LED_PIN, num_pixels, auto_write=False)

# Function to play a sound on the buzzer
def play_buzzer():
    buzzer.duty_cycle = 2 ** 15
    time.sleep(0.2)
    buzzer.duty_cycle = 0

# Function to move the servo
def move_servo(angle):
    duty_cycle = int(2 ** 15 + (angle / 180) * (2 ** 15))
    servo.duty_cycle = duty_cycle
    time.sleep(0.5)
    servo.duty_cycle = 0

# Function to turn on the LED strip
def turn_on_led():
    led_strip.fill((254, 2, 255))  # Set the color to red (you can change this)
    led_strip.fill((44, 45, 213))
    led_strip.show()

# Function to turn off the LED strip
def turn_off_led():
    led_strip.fill((0, 0, 0))  # Turn off all LEDs
    led_strip.show()

# Main loop
while True:
    if not button.value:  # Button is tapped (button value is False)
        play_buzzer()
        move_servo(90)  # Move the servo to the 90-degree position
        turn_on_led()
        time.sleep(0.5)  # Add a small delay to avoid multiple taps in quick succession
        turn_off_led()   # Turn off the LEDs after a short duration


