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

    def setLedArray(self, ledArray, color):
        ''' Sets Leds in certain positions to the given color'''
        for i in range(len(ledArray)):
            self.ledStrip.setPixelColor(i, color)
        self.ledStrip.show()

