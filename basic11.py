#date , time

import  cv2
import  datetime

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check, frame = cap.read()

    if check == True:
        date_time = datetime.datetime.now()
        cv2.putText(frame, date_time.strftime("%d %B %Y - %X"), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), cv2.LINE_4)
        cv2.imshow("output", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break




cap.release()
cv2.destroyAllWindows()