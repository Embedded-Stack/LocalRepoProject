from machine import Pin, ADC #type: ignore 
#ATTENUATION
import time

LDR = ADC(Pin(34))
LDR.atten(ADC.ATTN_11DB)
LDR.width(ADC.WIDTH_10BIT)
while True:
    brightness = LDR.read()
    print("Light : ", brightness)
    time.sleep(0.5)
