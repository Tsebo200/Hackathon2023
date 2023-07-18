# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
NeoPixel example for Pico. Turns the NeoPixels red.

REQUIRED HARDWARE:
* RGB NeoPixel LEDs connected to pin GP0.
"""
import board
import neopixel

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 110

pixels = neopixel.NeoPixel(board.GP17, num_pixels)
pixels.brightness = 0.5


while True:
    pixels.fill((255, 255, 255))


