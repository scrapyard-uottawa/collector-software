from rpi_ws281x import PixelStrip, Color
# LED strip configuration:
LED_COUNT = 120        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


class ledIndicator:
    def __init__(self,) -> None:
        '''
            Initializes the led strip
        '''
        self.ledStrip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.ledStrip.begin()

    def clearAllLeds(self):
        '''
            Clears all leds on the led strip
        Args:
            None
        Returns:
            None
            '''
        for i in range(self.ledStrip.numPixels()):
            self.ledStrip.setPixelColor(i, Color(0, 0, 0))
        self.ledStrip.show()

    def setAllLeds(self, color: Color) -> None:
        '''
            Sets all leds to the same color
        Args:
            color: the color to set the leds to
        Returns:
            None
            '''
        for i in range(self.ledStrip.numPixels()):
            self.ledStrip.setPixelColor(i, color)
        self.ledStrip.show()

    def setLedRoation(self, color=Color(0, 0, 255), wait_ms=50, iterations=10) -> None:
        '''
            Sets the color of the leds in a rotation
        Args:
            color: the color to set the leds to
        Returns:
            None
            '''
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.ledStrip.numPixels(), 3):
                    self.ledStrip.setPixelColor(i + q, color)
                self.ledStrip.show()
                self.ledStrip.sleep(wait_ms / 1000.0)
                for i in range(0, self.ledStrip.numPixels(), 3):
                    self.ledStrip.setPixelColor(i + q, 0)