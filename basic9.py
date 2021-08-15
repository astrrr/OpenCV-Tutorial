#วาดวงกลม

import  cv2

img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img, (700,700))


#วาดวงกลม
# circle (ภาพ, ตำแหน่งจุดศูนย์กลาง(x, y), รัศมี, สี(BGR), ความหนา)
#                                                    ความหนา(-1) = กล่องทึบ

cv2.circle(imgresize, (320, 250), 200, (255, 0, 0), 3)

cv2.imshow("Output", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()