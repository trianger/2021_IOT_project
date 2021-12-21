import cv2

#image 파일 읽기
img = cv2.imread('soulcompany.jpeg')
img2 = cv2.resize(img, (600, 400))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

#cv2.imshow('soulcompany', img)
#cv2.imshow('soulcompany1', img2)
#cv2.imshow('soulcompany2', gray)

cv2.imshow('soulcompany', edge1)
cv2.imshow('soulcompany1', edge2)
cv2.imshow('soulcompany2', edge3)
#키보드 입력을 기다림
#기본값 0, 0인 경우 키보드 입력이 있을 때까지 계속 기다림
cv2.waitKey(0)

while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('soulcompany2.jpeg', gray)
#열려있는 모든 창 닫기
cv2.destroyAllWindows()