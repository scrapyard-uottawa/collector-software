from ledIndicator import ledIndicator
from time import sleep

ledIndicator = ledIndicator()

ledIndicator.setLedArray([1,2,3,4,5,6,7,8,9,10], Color(255,0,0))
sleep(1)
ledIndicator.setLedArray([11,12,13,14,15,16,17,18,19,20], Color(0,255,0))
sleep(1)
ledIndicator.setLedArray([21,22,23,24,25,26,27,28,29,30], Color(0,0,255))