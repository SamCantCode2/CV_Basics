import cv2 as cv

def rescalesize(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dims = (width, height)
    return cv.resize(frame, dims, interpolation=cv.INTER_AREA)

def reschange(width, height, capture): #used for current video
    capture.set(3, width)
    capture.set(4, height)

#images
img = cv.imread(r'C:\Users\Samhruth\Pictures\Saved Pictures\ForEncry.jpeg')
imgresize = rescalesize(img)
cv.imshow('Sudo', img)
cv.waitKey(0)

capture = cv.VideoCapture(0)
reschange(100, 100, capture)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('d'): #plays as many seconds and waits for d key but in individual frames
        break

capture.release()
cv.destroyAllWindows()