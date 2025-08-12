import machine #type: ignore
import time

LED = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    if button.value() == 0:
        if LED.value() == 1:
            LED.value(0)
            time.sleep(2)
        else:
            LED.value(1)
            time.sleep(2)
    time.sleep(0.2)
        
