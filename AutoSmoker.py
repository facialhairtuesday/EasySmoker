# RPi Smoker Controller #
# FHT #
# V1.0 #
# 2018-06-19 #


# Add folders to system path to
# include other downloaded modules
# Change system path as required if modules
# are in a different folder than Home
# May need to add __init__.py file to folder
import sys
sys.path.insert(0,'/home/pi/')
#sys.path.insert(0,'/home/pi/MAX31865')

# Import Other Modules
import time
import I2C_LCD_driver as driver # Drives 2x16 LCD display
from MAX31865 import max31865 # Allows for connecting RPi to PTDs

csPin0 = 8 #CE0 Pin
csPin1 = 7 #CE1 Pin
misoPin = 9
mosiPin = 10
clkPin = 11

while True:
    # Get Temp from pointed tip PT100 probe
    pointyTemp = max31865.max31865(csPin0, misoPin, mosiPin, clkPin).readTemp()

    # Get Temp from blunt tip PT100 probe
    bluntTemp = max31865.max31865(csPin1, misoPin, mosiPin, clkPin).readTemp()

    print('Pointy temperature is: {}'.format(round(pointyTemp,1)))
    print('Blunt temperature is: {}'.format(round(bluntTemp,1)))

    # Start LCD Code
    mylcd = driver.lcd()

    # Setup DHT22 Sensor
    #sensor = Adafruit_DHT.DHT22
    #pin = 4

    # Get Temp & Humidity values (C & %)
    #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if pointyTemp is not None and bluntTemp is not None:
        print('Pointy Temp={0:0.1f}C Blunt Temp = {1:0.1f}%'.format(pointyTemp, bluntTemp))
        #print(round(temperature,2))
        #print(round(humidity,2))
    else:
        print('Failed to get reading. Try again!')

    # Display Temp & Humidity vals on LCD screen
    mylcd.lcd_display_string("Pointy: %0.1fC" % pointyTemp,1)
    mylcd.lcd_display_string("Blunt: %0.1fC" % bluntTemp,2)

    time.sleep(5)