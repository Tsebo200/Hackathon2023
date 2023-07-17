import board
import neopixel
pixels = neopixel.NeoPixel(board.GP18, 16)

pixels[0] = (0, 255, 255)