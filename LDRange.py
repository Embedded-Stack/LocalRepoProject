import machine #type: ignore
import time

LDR = machine.ADC(machine.Pin(34))
LDR.atten(machine.ADC.ATTN_11DB)
LDR.width(machine.ADC.WIDTH_10BIT)
LED = machine.Pin(2, machine.Pin.OUT)

while 1:
    data = LDR.read()
    if data > 900:
        LED.value(1)
    else:
        LED.value(0)
    time.sleep(0.2)