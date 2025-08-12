import machine #type: ignore
import time

LDR = machine.ADC(machine.Pin(34))
LDR.atten(machine.ADC.ATTN_11DB) #Full range: 0 - 3.3v
LDR.width(machine.ADC.WIDTH_10BIT) #10 - BIT resolution (0 - 1023)

while True:
    brightness = LDR.read() #read ADC value
    print("Brightness : ", brightness)
    time.sleep(0.5)