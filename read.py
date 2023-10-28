import cv2 as cv

def rescalesize(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dims = (width, height)
    return cv.resize(frame, dims, interpolation=cv.INTER_AREA)

#images
img = cv.imread(r'')
cv.imshow('Sudo', img)
cv.waitKey(0)

#capture = cv.VideoCapture(0) #integer for webcam (0) or connected cameras (1, 2, 3...)
capture = cv.VideoCapture(r'')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(5) & 0xFF == ord('d'): #plays 5 seconds and waits for d key
        break

capture.release()
cv.destroyAllWindows()
