import time
import RPi.GPIO as GPIO
import time
import buzzer
import dht11
import settings

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()                     # Release resource

buzzer.setup(21)

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=22)

# ...................................................................................................................................
while True:
    result = instance.read()
    try:
        if result.is_valid():
            settings.tempf = (result.temperature*1.8)+32
            print("Temp: %d F" % settings.tempf +' '+"Humid: %d %%" % result.humidity)
            time.sleep(1)
            
            if settings.tempf > 78:
                buzzer.beep(.2)
            
            time.sleep(1)
            
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
