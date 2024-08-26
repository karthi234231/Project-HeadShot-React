import cv2

pengklasifikasiWajah = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
videoCam = cv2.VideoCapture(0)

if not videoCam.isOpened():
    print("Camera Cap not opened or camera doesn't work")
    exit()

tombolQditekan = False
while not tombolQditekan:
    ret, kerangka = videoCam.read()
    if ret:
        abuAbu = cv2.cvtColor(kerangka, cv2.COLOR_BGR2GRAY)
        dafWajah = pengklasifikasiWajah.detectMultiScale(abuAbu, scaleFactor=1.3, minNeighbors=2)
        for (x, y, w, h) in dafWajah:
            cv2.rectangle(kerangka, (x, y), (x + w, y + h), (0, 255, 0), 2)
        teks = "Face Count = " + str(len(dafWajah))
        cv2.putText(kerangka, teks, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
        cv2.imshow("Hasil", kerangka)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            tombolQditekan = True

videoCam.release()
cv2.destroyAllWindows()
