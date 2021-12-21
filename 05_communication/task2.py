from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

display = drivers.Lcd()

try:
    print("Writing to display")
    while True:
        now = datetime.datetime.now()
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            display.lcd_display_string(now.strftime("%x%X"), 1)
            display.lcd_display_string(f'{t:.1f}%*C, {h:.1f}%', 2)
        else :
            print('Read Error')
        print(now.strftime("%x %X"))
        time.sleep(1)
finally:
    print("Cleaning up!")
    display.lcd_clear()