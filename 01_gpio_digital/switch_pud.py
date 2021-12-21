import RPi.GPIO as GPIO
import time

switch_pin = 18

GPIO.setmode(GPIO.BCM)
#내부풀업저항사용하기
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)#UP/DOWN
#GPIO.setup(switch_pin)
try:
    while True:
        val = GPIO.input(switch_pin)
        print(val)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')