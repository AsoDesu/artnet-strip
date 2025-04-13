from rpi_ws281x import *
from artnet import ArtNetReceiver
from ledstrip import LedStrip

# CONFIG
LED_COUNT       = 100     # Number of LED pixels.
PATCH_UNIVERSE  = 5       # The DMX Universe to listen on
PATCH_ADDRESS   = 0       # The DMX Address to start at
LED_PIN         = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ     = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA         = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS  = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT      = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL     = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip: LedStrip

def main():
    print("Starting Island Co. LED Strip")

    pixel_strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip = LedStrip(LED_COUNT, PATCH_ADDRESS, pixel_strip)

    artnet = ArtNetReceiver(data_method=strip.on_dmx_data, universe=PATCH_UNIVERSE)

    while True:
        try:
            cmd = input()
        except:
            break
    print("Goodbye <3")
    strip.close()
    artnet.disconnect()

if __name__ == "__main__":
    main()