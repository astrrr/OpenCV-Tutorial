#บันทึก video

import  cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #ตั้งค่า four cc

result = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480)) #เตรียม file

while (cap.isOpened()):
    check, frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
   
    if check == False :
        break
    else:
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #เปลี่ยนสีเป็น grayscale
        cv2.imshow("Output",frame)
        result.write(frame)   #เขียน video ลงใน file ที่เตรียมไว้
        if cv2.waitKey(1) & 0xFF == ord("w"):
            break


    

    
#คืน resource ให้เครื่อง
result.release()
cap.release() 
cv2.destroyAllWindows()