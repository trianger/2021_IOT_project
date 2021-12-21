import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#pwm 인스턴트 생성, 주파수설정
#1초에 50번 사이클을 돌게 하겠다.
pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0)

try:
    for i in range(3):
        for i in range(0,101, 5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
            #서서히 꺼짐
        for i in range(100, -1, -5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
finally:
    pwm.stop()
    GPIO.cleanup()
    print('cleanup and exit')
