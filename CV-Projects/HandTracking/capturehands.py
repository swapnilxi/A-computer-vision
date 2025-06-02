import cv2


cap= cv2.VideoCapture(0) 
cap=  set(4,1280)
cap=  set(3,720)

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to capture frame")
        break

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()