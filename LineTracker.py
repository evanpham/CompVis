import cv2
import numpy as np


def findLine(image):
    # Convert to binary image, and find all black pixels (the line)
    # Blurring and re-binarying helps remove false black pixels
    bw = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)[1]
    bw = cv2.blur(bw, (10, 10))
    bw = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)[1]
    pixels = np.argwhere(bw == 0)

    return pixels


# Set an image name for each frame and an frame number
frameNum = 0
imgName = "frame" + str(frameNum) + ".png"

# Create VideoCapture object for frame iteration and find frame dimensions
cap = cv2.VideoCapture('raw_video_feed.mp4')
w = cap.get(3)  # Width in pixels, float
h = cap.get(4)  # Height in pixels, float

# Iterate on frames
while cap.isOpened():
    ret, frame = cap.read()

    # If frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Find coordinates of pixels on line
    pixels = findLine(frame)

    # Get all black pixels in the bottom 100 rows
    pixels = pixels[pixels[:, 1] < 100]
    xPos = np.mean(pixels[:, 0])
    yPos = np.mean(pixels[:, 1])

    # Place white circle on center of line at bottom and show the frame
    cv2.circle(frame, (int(w-xPos), int(h-20)), 10, (0, 200, 0), -1)
    cv2.imshow('frame', frame)

    # Can quit playback with q
    if cv2.waitKey(1) == ord('q'):
        break

    # Save frame as image in /Frames and update img name for next frame
    status = cv2.imwrite("Frames/" + imgName, frame)
    imgName = imgName.replace(str(frameNum), str(frameNum + 1))
    frameNum += 1

# End video capture and playback
cap.release()
cv2.destroyAllWindows()
