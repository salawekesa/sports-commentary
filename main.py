import cv2
import pytesseract
from gtts import gTTS
from playsound import playsound

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# video = cv2.VideoCapture('https://10.1.129.161:8080/video')
# video.set(3, 640)
# video.set(4, 480)

img1 = cv2.imread('Capture_1.JPG')
img2 = cv2.imread('Capture_2.JPG')
img3 = cv2.imread('Capture_3.JPG')

h1Img, w1Img, none1 = img1.shape
h2Img, w2Img, none2 = img2.shape
h3Img, w3Img, none3 = img3.shape

box1 = pytesseract.image_to_boxes(img1)
box2 = pytesseract.image_to_boxes(img2)
box3 = pytesseract.image_to_boxes(img3)

data1 = pytesseract.image_to_data(img1)
data2 = pytesseract.image_to_data(img2)
data3 = pytesseract.image_to_data(img3)

filewrite = open("String.txt", "w")
for z, a in enumerate(data1.splitlines()):
        if z != 0:
            a = a.split()
            if len(a) == 12:
                x, y = int(a[6]), int(a[7])
                w, h = int(a[8]), int(a[9])
                cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(img1, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
                filewrite.write(a[11] + " ")
filewrite.close()
fileread = open("String.txt", "r")
language = 'en'
line = fileread.read()
if line != " ":
    fileread.close()
    speech = gTTS(text=line, lang=language, slow=False)
    speech.save("test.mp3")
cv2.imshow('gtts', img1)
cv2.waitKey(0)
playsound("test.mp3")



# while True:
#     extra, frames = video.read()
#     data4 = pytesseract.image_to_data(frames)
#     filewrite = open("String.txt", "w")
#     for z, a in enumerate(data4.splitlines()):
#         if z != 0:
#             a = a.split()
#             if len(a) == 12:
#                 x, y = int(a[6]), int(a[7])
#                 w, h = int(a[8]), int(a[9])
#                 cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)
#                 cv2.putText(frames, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
#     cv2.imshow('Video capture', frames)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         video.release()
#         cv2.destroyAllWindows()
#         break





# for z, a in enumerate(data1.splitlines()):
#     if z != 0:
#         a = a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w, h = int(a[8]), int(a[9])
#             cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 1)
#             cv2.putText(img1, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
#
# for z, a in enumerate(data2.splitlines()):
#     if z != 0:
#         a = a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w, h = int(a[8]), int(a[9])
#             cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 1)
#             cv2.putText(img2, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
#
# for z, a in enumerate(data3.splitlines()):
#     if z != 0:
#         a = a.split()
#         if len(a) == 12:
#             x, y = int(a[6]), int(a[7])
#             w, h = int(a[8]), int(a[9])
#             cv2.rectangle(img3, (x, y), (x + w, y + h), (0, 0, 255), 1)
#             cv2.putText(img3, a[11], (x - 15, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)
#
# cv2.imshow('capture 1', img1)
# cv2.imshow('capture 2', img2)
# cv2.imshow('capture 3', img3)
# cv2.waitKey(0)






# for a in box1.splitlines():
#     a = a.split()
#     x, y = int(a[1]), int(a[2])
#     w, h = int(a[3]), int(a[4])
#
#     cv2.rectangle(img1, (x, h1Img - y), (w, h1Img - h), (0, 0, 255), 1)
#
#     cv2.putText(img1, a[0], (x, h1Img - y - 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
#
# for a in box2.splitlines():
#     a = a.split()
#     x, y = int(a[1]), int(a[2])
#     w, h = int(a[3]), int(a[4])
#
#     cv2.rectangle(img2, (x, h1Img - y), (w, h1Img - h), (0, 0, 255), 1)
#
#     cv2.putText(img2, a[0], (x, h1Img - y - 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
#
# for a in box3.splitlines():
#     a = a.split()
#     x, y = int(a[1]), int(a[2])
#     w, h = int(a[3]), int(a[4])
#
#     cv2.rectangle(img3, (x, h1Img - y), (w, h1Img - h), (0, 0, 255), 1)
#
#     cv2.putText(img3, a[0], (x, h1Img - y - 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
#
# cv2.imshow('Image 1', img1)
# cv2.imshow('Image 2', img2)
# cv2.imshow('Image 3', img3)
#
# cv2.waitKey(0)
