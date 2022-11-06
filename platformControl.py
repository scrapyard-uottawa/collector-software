from BinType import BinType

# Variables
stepsPerBin = 100

class platformControl:
    # https://makersportal.com/blog/raspberry-pi-stepper-motor-control-with-nema-17

    def __init__(self) -> None:
        self.currentPosition = 0
        self.calibratePlatform()        
        pass

    def calibratePlatform(self):
        self.currentPosition = 1
        pass

    def updatePosition(self, binType: BinType):

        # Get the position of the 
        requestedPosition = binType.value
        relativeAdjustment = requestedPosition - self.currentPosition

        if relativeAdjustment > 0:
            self.movePlatform(True, relativeAdjustment* stepsPerBin)
        elif relativeAdjustment < 0:
            self.movePlatform(False, relativeAdjustment * - stepsPerBin)


        self.currentPosition = requestedPosition

    def movePlatform(self, direction: bool, relativeAdjustment: int):
        # MOTOR CODE FROM   https://makersportal.com/blog/raspberry-pi-stepper-motor-control-with-nema-17

        pass


       
    
b = platformControl()
b.movePlatform(BinType.GARBAGE)
b.movePlatform(BinType.COMPOST)
b.movePlatform(BinType.BLACK_BIN)
b.movePlatform(BinType.BLUE_BIN)
b.movePlatform(BinType.GARBAGE)
b.movePlatform(BinType.BLUE_BIN)
