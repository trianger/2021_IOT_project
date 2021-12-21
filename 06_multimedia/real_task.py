import RPi.GPIO as GPIO
import cv2
import time

SWITCH_PIN = 12                   #핀 번호 지정
BUZZER_PIN = 13
LED_PIN =11
SEGMENT_PINS = [4,5,6,7,8,9,10]
GPIO.setmode(GPIO.BCM)   #BCM 모드로 설정
GPIO.setup(SWITCH_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #스위치에 풀다운 저항 (눌렀을 때 on)
for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
# ㄴGPIO 장치들 셋업

pwm = GPIO.PWM(BUZZER_PIN, 262) #pwm 변수선언
cap = cv2.VideoCapture(0) # 장치열기
face_cascade = cv2.CascadeClassifier('./xml/face.xml') # 인공지능 분석 모듈

data = [[1, 1, 1, 1, 1, 1, 0],
[0, 1, 1, 0, 0, 0, 0],
[1, 1, 0, 1, 1, 0, 1],
[1, 1, 1, 1, 0, 0, 1],
[0, 1, 1, 0, 0, 1, 1],
[1, 0, 1, 1, 0, 1, 1],
[1, 0, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 1, 1]]
#ㄴ 7segment 0~9까지 출력 배열 선언

if not cap.isOpened():
    print('Camera open failed') # 카메라 안 열렸을 시 탈출
    exit()

while True:
    ret, frame = cap.read() #카메라 변수 설정
    cnt=0 #인원 수 초기화

    if not ret:
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#회색 이미지로 변환
    faces = face_cascade.detectMultiScale(gray) #이미지 분석
    val = GPIO.input(SWITCH_PIN) # 스위치 변수

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)#사각형 출력
        cnt+=1 #인원 수 체크
    #print(cnt) 
    for i in range(len(SEGMENT_PINS)):
        if cnt>8 :
            GPIO.output(SEGMENT_PINS[i],data[9][i]) # 9 이상의 숫자일 경우 출력 9로 고정(오류 방지)
        else : 
            GPIO.output(SEGMENT_PINS[i],data[cnt][i]) # 사람 수 출력
        print('checked\n')

    if cnt>=5 and val==0:
        GPIO.output(LED_PIN, GPIO.HIGH) # 5명 이상이고 스위치가 눌리지 않았을 경우 빨간 LED와 피에조 부저 출력
        pwm.start(50) 
    else :
        GPIO.output(LED_PIN, GPIO.LOW)
        pwm.stop()
    time.sleep(0.1)
    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 13: # 엔터 시 종료
        break


#사용자 자원 해제
#out.release()
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()