import RPi.GPIO as GPIO
import dht11
import time
import settings

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=22)

# ...................................................................................................................................
def runTemp():
    result = instance.read()
    if result.is_valid():
        settings.tempf = (result.temperature*1.8)+32
        print("Temp: %d F" % settings.tempf +' '+"Humid: %d %%" % result.humidity)
        time.sleep(1)
