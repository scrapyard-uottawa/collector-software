import BinType

class chuteControl:

    def __init__(self) -> None:
        self.platformPosition = 0
        self.calibratePlatform()        
        pass

    def openChute(self):
        self.platformPosition = 0
        pass

    def closeChute(self, binType: BinType):
        pass
    
b = chuteControl()