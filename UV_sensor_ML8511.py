

from time import sleep
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

try:
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    chan = AnalogIn(ads, ADS.P0)
except:
    pass

def voltage_to_UV(chan, in_min,  in_max,  out_min,  out_max)

  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def read_UV():
    #those values are imported since dataShet 
    try:
        uvIntensity = mapfloat(outputVoltage, 0.99, 2.8, 0.0, 15.0); #Convert the voltage to a UV intensity level
        return uvIntensity
    except:
        return None

