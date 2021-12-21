from _typeshed import StrPath
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

try:
    while True:
        GPIO.output(TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.00001) #10us (1us -> 0.000001s)
        GPIO.output(TRIGGER_PIN, GPIO.LOW)

         #echo pin -> high로 되는 시작(시작시간)
        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()
        
        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()

        duration_time = stop - start
        distance = 17160*duration_time

        print('Distance : %.1fcm' % distance)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')