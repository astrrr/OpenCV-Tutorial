#วาดสี่เหลี่ยม

import  cv2

img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img, (700,700))


#วาดสี่เหลี่ยม
# rectangle (ภาพ, มุม1(บนซ้าย), มุม2(ล่างขวา), สี(BGR), ความหนา)
#                                                    ความหนา(-1) = กล่องทึบ

cv2.rectangle(imgresize, (170, 20), (450, 400), (0, 0, 255), 3)

cv2.imshow("Output", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()