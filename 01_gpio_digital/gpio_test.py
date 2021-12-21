import RPi.GPIO as GPIO
import time

SWITCH_PIN = 18 # 스위치 핀
TRIGGER_PIN = 17
ECHO_PIN = 27
LED_PIN = 23
LED_PIN2 = 24
LED_PIN3 = 4
BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)          #핀 번호를 BCM 기준으로 변경
GPIO.setup(SWITCH_PIN, GPIO.IN)   #스위치, LED, 부저, 초음파 센서 등 작동을 위한 활성화
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #스위치에 풀다운 저항 (눌렀을 때 on)
pwm = GPIO.PWM(BUZZER_PIN, 262)

try:
    while True:
        GPIO.output(TRIGGER_PIN, True)
        time.sleep(0.00001) #10us (1us -> 0.000001s) 10마이크로세컨드동안  HIGH 신호 부여
        GPIO.output(TRIGGER_PIN, False)

         #echo pin -> high로 되는 시작(시작시간)
        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()
        
        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()

        duration_time = stop - start # 초음파 받은 시간 - 초음파 발생 시간 = 거리에 비례한 시간 단위
        distance = 17160*duration_time # 거리 단위로 변환(속도를 곱함)

        val = GPIO.input(SWITCH_PIN)
        print("swtich :", val)
        
        print('Distance : %.1fcm' % distance) # 거리 출력
        #print('stop : %.1fcm' % stop)    <- 작동 여부 실험 중 활용한 주석
        #print('start : %.1fcm' % start)

        if distance <= 10 or val == 1:      # 거리가 10 이하일 경우 빨간 LED on, 부저 울림
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(LED_PIN2,GPIO.LOW)
            GPIO.output(LED_PIN3,GPIO.LOW)
            print('red led on')
            pwm.start(50) # 능동부저 스타트

        elif distance <= 20:               # 거리가 20 이하일 경우 노란색 LED on 
            GPIO.output(LED_PIN2, GPIO.HIGH)
            GPIO.output(LED_PIN,GPIO.LOW)
            GPIO.output(LED_PIN3,GPIO.LOW)
            print('yellow led on')
            pwm.stop() # 거리가 10이 아닌 경우 모두에 이 명령어를 넣어 부저가 멈추게 함
        elif distance <= 30:                # 거리가 30 이하일 경우 초록색 LED on 
            GPIO.output(LED_PIN3, GPIO.HIGH)
            GPIO.output(LED_PIN,GPIO.LOW)
            GPIO.output(LED_PIN2,GPIO.LOW)
            print('green led on')          
            pwm.stop()

        else :
            GPIO.output(LED_PIN,GPIO.LOW)
            GPIO.output(LED_PIN2,GPIO.LOW)
            GPIO.output(LED_PIN3,GPIO.LOW)
            print('led off')               # 거리가 30초과일 경우 아무런 출력 없음
            pwm.stop()
        time.sleep(0.1)
finally:                # 작동 중지
    GPIO.cleanup()
    print('cleanup')  