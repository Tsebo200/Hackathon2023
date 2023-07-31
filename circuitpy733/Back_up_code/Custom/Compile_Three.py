import time
import board
import digitalio
import pwmio
import neopixel
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.GP16, duty_cycle=3 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

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
buzzer = pwmio.PWMOut(BUZZER_PIN, duty_cycle=0)

# Initialize servo
# servo = pwmio.PWMOut(SERVO_PIN, duty_cycle=2 ** 15, frequency=50)

# Initialize LED strip
num_pixels = 110  # Change this to the number of LEDs in your strip
led_strip = neopixel.NeoPixel(LED_PIN, num_pixels, auto_write=False)

# initialise Motor
motor =  digitalio.DigitalInOut(MOTOR_PIN)
motor.direction = digitalio.Direction.OUTPUT


# Function to play a sound on the buzzer
def play_buzzer():
    buzzer.duty_cycle = 2 ** 15
    time.sleep(0.2)
    buzzer.duty_cycle = 0

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

def onServo_turn():
    for angle in range(0, 90, 90):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(1)
    for angle in range(90, 0, -90): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(1)


# Main loop
while True:
    if  button.value:  # Button is tapped (button value is False)
        play_buzzer()
        # move_servo(90)  # Move the servo to the 90-degree position
        turn_on_led()
        motor_on()
        time.sleep(5)  # Add a small delay to avoid multiple taps in quick succession
        turn_off_led()   # Turn off the LEDs after a short duration
        motor_off()
        onServo_turn()





import time
import board
import pwmio

# Define pin number for the buzzer
BUZZER_PIN = board.A1

# Initialize PWMOut for the buzzer
buzzer_pwm = pwmio.PWMOut(BUZZER_PIN, frequency=440, duty_cycle=0)

# Function to play a note on the buzzer
def play_note(note_frequency, note_duration):
    buzzer_pwm.frequency = note_frequency
    buzzer_pwm.duty_cycle = 2 ** 15
    time.sleep(note_duration)
    buzzer_pwm.duty_cycle = 0

# Function to stop the buzzer sound
def stop_buzzer():
    buzzer_pwm.duty_cycle = 0

# Map notes to their corresponding frequencies (Hz)
NOTE_C4 = 261.63
NOTE_D4 = 293.66
NOTE_E4 = 329.63
NOTE_F4 = 349.23
NOTE_G4 = 392.00
NOTE_A4 = 440.00
NOTE_B4 = 493.88
NOTE_REST = 0  # Represents a rest (no sound)

# Define the "Happy Birthday" tune as a list of notes and durations
happy_birthday_tune = [
    (NOTE_C4, 0.2),
    (NOTE_C4, 0.2),
    (NOTE_D4, 0.4),
    (NOTE_C4, 0.4),
    (NOTE_F4, 0.4),
    (NOTE_E4, 0.8),
    (NOTE_REST, 0.2),
    (NOTE_C4, 0.2),
    (NOTE_C4, 0.2),
    (NOTE_D4, 0.4),
    (NOTE_C4, 0.4),
    (NOTE_G4, 0.4),
    (NOTE_F4, 0.8),
    (NOTE_REST, 0.2),
    (NOTE_C4, 0.2),
    (NOTE_C4, 0.2),
    (NOTE_C5, 0.4),
    (NOTE_A4, 0.4),
    (NOTE_F4, 0.4),
    (NOTE_E4, 0.4),
    (NOTE_D4, 0.4),
    (NOTE_B4, 0.4),
    (NOTE_REST, 0.2),
    (NOTE_G4, 0.2),
    (NOTE_G4, 0.2),
    (NOTE_F4, 0.4),
    (NOTE_D4, 0.4),
    (NOTE_E4, 0.4),
    (NOTE_C4, 0.4),
    (NOTE_C4, 0.8),
]

# Main loop to play the tune
while True:
    for note_frequency, note_duration in happy_birthday_tune:
        if note_frequency == NOTE_REST:
            stop_buzzer()  # If it's a rest, stop the buzzer
        else:
            play_note(note_frequency, note_duration)
        time.sleep(0.1)  # Add a small delay between notes
