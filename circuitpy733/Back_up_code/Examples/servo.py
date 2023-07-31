delay_ms = 25  # Amount of milliseconds to wait between servo movements



while True:
    for position in range(0, 180):  # Step the position forward from 0deg to 180deg
        print(position)  # Show the current position in the Shell/Plotter
        my_servo.write(position)  # Set the Servo to the current position
        time.sleep_ms(delay_ms)  # Wait for the servo to make the movement
    
    for position in reversed(range(0, 180)):  # Step the position reverse from 180deg to 0deg
        print(position)  # Show the current position in the Shell/Plotter
        my_servo.write(position)  # Set the Servo to the current position
        time.sleep_ms(delay_ms)  # Wait for the servo to make the movement  