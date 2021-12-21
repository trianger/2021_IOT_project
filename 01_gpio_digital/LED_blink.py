import RPi.GPIO as GPIO
import time

LED_PIN = 7
a = 8
b = 9

GPIO.setmode(GPIO.BCM)          # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN, GPIO.OUT)  #GPIO.OUT OR GPIO.IN
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
for i in range(1):
    GPIO.output(b, GPIO.HIGH) #1
    print("led on")
    time.sleep(2)
    GPIO.output(b, GPIO.LOW) # 0
    print("led off")
    #time.sleep(0)

for i in range(1):
    GPIO.output(8, GPIO.HIGH) #1
    print("led on")
    time.sleep(2)
    GPIO.output(8, GPIO.LOW) # 0
    print("led off")
    #time.sleep(2)

for i in range(1):
    GPIO.output(LED_PIN, GPIO.HIGH) #1
    print("led on")
    time.sleep(2)
    GPIO.output(LED_PIN, GPIO.LOW) # 0
    print("led off")
    #time.sleep(2)
GPIO.cleanup() #GPIO 핀상태 초기화