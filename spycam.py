import cv2

capture = cv2.VideoCapture(0)
duration = int(input("The Duration of the Video: "))
duration = duration*10
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = cv2.VideoWriter('video.avi', fourcc, 30.0, (640, 480))
current = 0
limit = 3*duration # by duration 50 ca. 50 seconds

while(True):

    ret, frame = capture.read()

    if ret:
        videoWriter.write(frame)

    if current == limit:
        break
    else:
        current += 1
        print(current)

capture.release()
videoWriter.release()

cv2.destroyAllWindows()
