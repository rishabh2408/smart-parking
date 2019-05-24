from PIL import Image
import pytesseract
import cv2
# capture image
def ocr():
	im= Image.open("plate.png")
	text= pytesseract.image_to_string(im, lang='eng')
	print(text)
if __name__=="__main__":
	ocr()