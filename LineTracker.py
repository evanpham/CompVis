import cv2
import numpy as np

# Set an image name for each frame and an index to track frame order
index = 0
imgName = "frame0.png"
height, width = 0, 0

# Create VideoCapture object for frame iteration
cap = cv2.VideoCapture('raw_video_feed.mp4')

# Iterate on frames
while cap.isOpened():
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    
    if (height, width == 0, 0):
        height, width = bw.shape[:2]
    
    pixels = np.argwhere(bw == 0)

    pixels = pixels[pixels[:, 1] < 100]
    xPos = np.mean(pixels[:, 0])

    cv2.circle(gray, (width-int(xPos), height-20), 10, (255, 255, 255), -1)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break

    status = cv2.imwrite("Frames/" + imgName, gray)
    imgName = imgName.replace(str(index), str(index + 1))
    index += 1
    
cap.release()
cv2.destroyAllWindows()

height, width = bw.shape[:2]
print(width)
print(height)
pixels = np.argwhere(bw == 255)

pixels = pixels[pixels[:, 1] > 140]
xPos = np.mean(pixels[:, 0])
yPos = np.mean(pixels[:, 1])

print(xPos)
print(yPos)
