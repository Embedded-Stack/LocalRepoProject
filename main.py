import machine #type: ignore
import time
led = machine.Pin(2, machine.Pin.OUT)
ldr = machine.ADC(machine.Pin(34))
ldr.width(machine.ADC.WIDTH_10BIT)
ldr.atten(machine.ADC.ATTN_11DB)
prev = 0

while True:
    value = ldr.read()
    if value != prev:
        print("ADC  = ",1023 - value)
        prev = value
        time.sleep(0.5)
        led.off()
    else:
        led.on()
    