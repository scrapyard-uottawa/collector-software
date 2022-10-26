import RPi.GPIO as GPIO
import time


class motorController:
    def __init__(self) -> None:
        self.motorR = 9
        self.motorL = 10

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motorR, GPIO.OUT)
        GPIO.setup(self.motorL, GPIO.OUT)
        
        GPIO.output(self.motorR, GPIO.LOW)
        GPIO.output(self.motorL, GPIO.LOW)


    def moveRight(self):
        GPIO.output(self.motorR, GPIO.HIGH)
        GPIO.output(self.motorL, GPIO.LOW)
        time.sleep(20)
        GPIO.output(self.motorR, GPIO.LOW)
        GPIO.output(self.motorL, GPIO.LOW)

    def moveLeft(self):
        GPIO.output(self.motorR, GPIO.LOW)
        GPIO.output(self.motorL, GPIO.HIGH)
        time.sleep(20)
        GPIO.output(self.motorR, GPIO.LOW)
        GPIO.output(self.motorL, GPIO.LOW)