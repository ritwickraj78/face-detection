import cv2
detect = cv2.CascadeClassifier("1.2 haarcascade_frontalface_default.xml")
imp_img = cv2.VideoCapture("elon.jpg")
res, img = imp_img.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detect.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 5)
cv2.imshow("elon image", img)
cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()
