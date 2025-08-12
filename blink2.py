import machine as esp32 #type: ignore
import time as t

OUTPUT = esp32.Pin.OUT
PIN = esp32.Pin
LED = PIN(2, OUTPUT)
DELAY = t.sleep
while True:
    LED.value(1)
    DELAY(0.1)
    LED.value(0)
    DELAY(0.1)
