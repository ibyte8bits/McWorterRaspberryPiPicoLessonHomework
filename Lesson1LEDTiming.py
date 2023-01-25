from machine import Pin
from time import ticks_us
myLED = Pin('LED',Pin.OUT)

print(ticks_us())
startTime = ticks_us()
myLED.value(1)
myLED.value(0)
endtime = ticks_us() - startTime
print(ticks_us())
print(endtime)