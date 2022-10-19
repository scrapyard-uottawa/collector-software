from rpi_ws281x import PixelStrip, Color
# LED strip configuration:
LED_COUNT = 120        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal
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

    def setLedArray(self, startLed: int, endLED: int, color: Color) -> None:
        '''
            Sets the color of certain leds in the led strip
        Args:
            startLED: the first led to set
            endLED: the last led to set
            color: the color to set the leds to
        Returns:
            None
        '''
        for i in range(startLed, endLED):
            self.ledStrip.setPixelColor(i, color)
        self.ledStrip.show()

    def setGarbageType(self, garbageType: str) -> None:
        ''' Sets the color of the leds to the color of the garbage type
        Args:
            garbageType: the type of garbage to set the leds to
        Returns:
            None
        Throws:
            KeyError: if the garbageType has not been declared led_pixel_config
        '''
        self.clearAllLeds()
        # Check if the garbage type is valid
        if garbageType in led_pixel_config:
            pixelC = led_pixel_config[garbageType]
            self.setLedArray(pixelC["start"], pixelC["end"], pixelC["color"])

        # Throw an error if the garbage type is not valid
        else:
            raise ValueError("Invalid garbage type")
