import machine #type: ignore
import time

led = machine.PWM(machine.Pin(2))
led.freq(500)

while 1:
    for i in range(0, 1023, 50):
        led.duty(i)
        time.sleep(0.05)
    for i in range(1023, 0, -50):
        led.duty(i)
        time.sleep(0.05)