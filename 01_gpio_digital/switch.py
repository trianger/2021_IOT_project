import RPi.GPIO as GPIO
import time

SWITCH_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        time.sleep(0.1)

finally :
    GPIO.setup(SWITCH_PIN, GPIO.OUT)
    GPIO.cleanup() 
    print("clean up and exit")