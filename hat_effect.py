import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('hat.png')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.1, 5, 30)
    
    for (x,y,w,h) in faces:
        hf = frame[0:y, x:x+w]
        hx, hy, _ = hf.shape
        hat = cv2.resize(img, (hy, hx))

        result = cv2.add(hf, hat)
        gray_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        
        


        for i in range(hx):
            for j in range(hy):
                if gray_result[i][j] == 255:
                    result[i][j] = [0,0,0]

        frame[0:y, x:x+w] = result
        

 
    cv2.imshow('hat_effect', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
