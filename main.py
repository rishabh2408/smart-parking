import cv2

plate_classifier = cv2.CascadeClassifier('C:/Users/Jain/Desktop/major/facerecog/haarcascade_licence_plate_rus_16stages.xml')
img=cv2.imread('test.jpg',0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plate = plate_classifier.detectMultiScale(gray,1.3,5)
if plate is():
	print("nada")
for(x,y,w,h) in plate:
	cropped_plate = img[y:y+h, x:x+w]
	imwrite("read.jpg",cropped_plate)