from ledIndicator import ledIndicator
from time import sleep

ledIndicator = ledIndicator()

while True:
    ledIndicator.setGarbageType("blackBin")
    sleep(5)
    ledIndicator.setGarbageType("blueBin")
    sleep(5)
    ledIndicator.setGarbageType("garbage")
    sleep(5)
    ledIndicator.setGarbageType("compost")
    sleep(5)