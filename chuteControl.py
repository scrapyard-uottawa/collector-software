import BinType

class chuteControl:

    def __init__(self) -> None:

        self.chuteIsOpen = False

        pass

    def openChute(self):
        if(self.chuteIsOpen == False):
            # open the chute
            self.chuteIsOpen = True

        pass
    
    def closeChute(self):
        #if chute is open then close it
        if(self.chuteIsOpen == True):
            # close the chute
            self.chuteIsOpen = False
        pass
    
b = chuteControl()