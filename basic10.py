#text

import  cv2

img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img, (700,700))


#ข้อความบนภาพ
# putText (ภาพ, ข้อความ, ตำแหน่งที่แสดงข้อความ(x, y), font, ขนาด, สี(BGR), ความหนา)
#                                                    ความหนา(-1) = กล่องทึบ

cv2.putText(imgresize, "Hello", (0, 100), 3, 4, (255, 128, 0), 3 )

cv2.imshow("Output", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()