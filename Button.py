import machine #type: ignore
import time

button = machine.Pin(4,machine.Pin.IN,machine.Pin.PULL_UP)

while True:
    if button.value() == 0 : 
        #button pressed
        machine.Pin(2, machine.Pin.OUT).value(1)
        print("Button Pressed!")
        time.sleep(2)
    else:
        machine.Pin(2, machine.Pin.OUT).value(0)
        print("Button Released!")
    time.sleep(0.2)