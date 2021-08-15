#วาดเส้น

import  cv2

img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img, (700,700))


#วาดเส้นตรง
# line (ภาพ, จุดเริ่มต้น(x, y), จุดสุดท้าย(x, y), สี(BGR), ความหนา)

cv2.arrowedLine(imgresize, (0, 0), (150,100), (255, 0, 0), 5)
cv2.arrowedLine(imgresize, (700, 0), (150,100), (0, 255, 0), 5)
cv2.arrowedLine(imgresize, (700, 450), (150,100), (0, 0, 255), 5)

cv2.imshow("Output", imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()