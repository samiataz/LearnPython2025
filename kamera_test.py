import cv2

cap = cv2.VideoCapture(1)  # USB kame

if not cap.isOpened():
    print("Kamera acilmadi.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret or frame is None or frame.size == 0:
        print("Kare alinamadi.")
        break

    cv2.imshow("USB Kamera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()