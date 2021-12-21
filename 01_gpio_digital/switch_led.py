import RPi.GPIO as GPIO
import time 

LED_PIN1 = 2
LED_PIN2 = 3
LED_PIN3 = 4

switch_pin1 = 14
switch_pin2 = 15
switch_pin3 = 18


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(switch_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(switch_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(switch_pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        val1 = GPIO.input(switch_pin1) #누르지 않은 경우 0, 눌렀을 때는 1
        val2 = GPIO.input(switch_pin2)
        val3 = GPIO.input(switch_pin3)
        print(val1, val2, val3)
        time.sleep(0.1)
        GPIO.output(LED_PIN1, val1) #GPIO.HIGH (1), GPIO.LOW (0)
        GPIO.output(LED_PIN2, val2)
        GPIO.output(LED_PIN3, val3)
finally:
    GPIO.cleanup()
    print("cleanup and exit")