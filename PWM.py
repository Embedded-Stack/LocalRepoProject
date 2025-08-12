import machine #type: ignore
import time

led = machine.PWM(machine.Pin(2))
led.freq(1000) #1khz

while True:
    for duty in range(0, 1024, 50):
        led.duty(duty)
        time.sleep(0.1)
    for duty in range(1023, 0, -50):
        led.duty(duty)
        time.sleep(0.1)