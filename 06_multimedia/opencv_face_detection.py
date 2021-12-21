import cv2

#분류기 파일로그
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

#Gray스케일 이미지로 변환
img = cv2.imread('avengers.jpg')
img = cv2.resize(img, (600, 300))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#gray = cv2.resize(img, (600, 300))
#이미지에서 얼굴 검출
faces = face_cascade.detectMultiScale(gray)

#얼굴 위치에 대한 좌표 정보 가져오기
for (x,y,w,h) in faces:
    #원본 이미지에 얼굴 위치 표시
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    #cv2.rectangle(gray, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
#cv2.imshow('gray', gray)
while True:
    if cv2.waitKey() == 13:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
