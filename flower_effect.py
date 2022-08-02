import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('flower.png')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.1, 5, 30)
    
    for (x,y,w,h) in faces:
        ff = frame[y:(y+h)-y//4, x-x//6:x+w//6]
        fx, fy, _ = ff.shape
        try:
            flower = cv2.resize(img, (fy, fx))
            result = cv2.add(ff, flower)
            gray_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)  
            for i in range(fx):
                for j in range(fy):
                    if gray_result[i][j] == 255:
                        result[i][j] = [0,0,0]
            frame[y:(y+h)-y//4, x-x//6:x+w//6] = result
        except:
            continue
    cv2.imshow('flower_effect', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
