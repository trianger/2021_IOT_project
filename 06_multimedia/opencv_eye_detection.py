import cv2

#분류기 파일로그
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

#Gray스케일 이미지로 변환
img = cv2.imread('avengers.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# = cv2.resize(img, (1000, 700))
#이미지에서 얼굴 검출
faces = face_cascade.detectMultiScale(gray)

#얼굴 위치에 대한 좌표 정보 가져오기
for (x,y,w,h) in faces:
    #원본 이미지에 얼굴 위치 표시
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    #ROI (region of interest, 관심영역)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    #눈 검출
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # 눈 위치에 대한 좌표정보 가져오기
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex-ew, ey-eh), (0, 255, 0), 2)

cv2.imshow('img', img)

while True:
    if cv2.waitKey() == 13:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
