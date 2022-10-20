from ledIndicator import ledIndicator
from time import sleep

ledIndicator = ledIndicator()

ledIndicator.setAllLeds(Color(255, 255, 255))
sleep(10)
ledIndicator.clearAllLeds()
sleep(2)
ledIndicator.setLedRoation()
sleep(20)