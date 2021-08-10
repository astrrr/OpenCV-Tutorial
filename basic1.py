import cv2

#อ่านภาพ
img = cv2.imread("image/cat.jpg")
'''print(type(img.ndim))  
print(img)'''

#รูปแบบภาพ ใส่ 0 ต่อท้าย imread จะเป็นภาพ grayscale 
imgGray = cv2.imread("image/cat.jpg",0)

#เปลียนขนาดภาพที่แสดงผล
imgResize = cv2.resize(imgGray, (400,300))

#แสดงผลภาพ
cv2.imshow("Output", imgResize)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()


