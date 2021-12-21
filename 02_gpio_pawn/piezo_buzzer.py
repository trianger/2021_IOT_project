# 도 음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#PWM 인스턴스 생성
#주파수 262HZ
pwm = GPIO.PWM(BUZZER_PIN, 262) #도는 262, 솔은 392
pwm.start(50)   #duty cycle 지정(0~100)
# dutycycle = (일정 주기에서 1상태가 지속되는 기간)
##time.sleep(2)
melody = [262, 294, 330, 349, 392, 440, 494, 523]
school =[392, 392, 440, 440, 392, 392, 330, 330, 392, 392, 330, 330, 294, 294]
school2 = [392, 392, 440, 440, 392, 392, 330, 330, 392, 330, 294, 330, 262]
try: 
    for i in school:
        pwm.ChangeFrequency(i)   # 주파수 변경, frequency = 주파수
        time.sleep(0.5)
    time.sleep(1)
    for i in school2:
        pwm.ChangeFrequency(i)   # 주파수 변경, frequency = 주파수
        time.sleep(0.5)
finally:
    pwm.stop()
    GPIO.cleanup()
    