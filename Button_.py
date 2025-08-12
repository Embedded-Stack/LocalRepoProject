import machine #type: ignore
import time
button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    if button.value() == 0:
            print("Button Pressed!")
            time.sleep(0.2)