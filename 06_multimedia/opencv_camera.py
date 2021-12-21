import cv2
 
cap = cv2.VideoCapture('output.avi') # 장치열기

if not cap.isOpened():
    print('Camera open failed')
    exit()

#cv2.VideoWriter_fourcc(*'D','I','V','X')

#fourcc = cv2.VideoWriter_fourcc(*'DIVX')

#out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))


#사진찍기
#ret, frame = cap.read()
#cv2.imwrite('output',frame)
#cv2.waitKey(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    #out.write(frame)

    if cv2.waitKey(10) == 13:
        break


#사용자 자원 해제
#out.release()
cap.release()
cv2.destroyAllWindows()