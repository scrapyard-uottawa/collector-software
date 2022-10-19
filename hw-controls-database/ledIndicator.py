from rpi_ws281x import PixelStrip, Color
import time

# LED strip configuration:
LED_COUNT = 120        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

led_pixel_config = {
    "blackBin": {
        "start": 0,
        "end": 10,
        "color": Color(255, 0, 0)
    },
    "blueBin": {
        "start": 10,
        "end": 20,
        "color": Color(0, 255, 0)
    },
    "garbage": {
        "start": 20,
        "end": 30,
        "color": Color(0, 0, 255)
    },
    "compost": {
        "start": 30,
        "end": 40,
        "color": Color(255, 255, 0)
    }
}   



class ledIndicator:
    def __init__(self,) -> None:
        '''
        Constructor
        '''
        self.ledStrip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.ledStrip.begin()
        pass

    def clearAllLeds(self):
        for i in range(self.ledStrip.numPixels()):
            self.ledStrip.setPixelColor(i, Color(0,0,0))
        self.ledStrip.show()

    def setLedArray(self, min,max, color):
        ''' Sets Leds in certain positions to the given color'''
        for i in range(min,max):
            self.ledStrip.setPixelColor(i, color)
        self.ledStrip.show()

    def setGarbageType(self, type):
        ''' Sets the color of the led strip to the color of the given garbage type'''
        self.clearAllLeds()
        self.setLedArray(led_pixel_config[type]["start"], led_pixel_config[type]["end"], led_pixel_config[type]["color"])