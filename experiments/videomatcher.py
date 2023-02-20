import cv2 as cv
import numpy as np
import csv
from matplotlib import pyplot as plt


#img = cv.imread('frame_true2_smaller.jpg',0)
cap = cv.VideoCapture('P-F05_Homework_Merged.mp4')
#img2 = img.copy()
template = cv.imread('template2.jpg',0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
#methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR','cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# Loop until the end of the video
frame_no = 0
last_frame_found_match = False
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    frame_no += 1
    # frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
    #                      interpolation = cv2.INTER_CUBIC)

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    img = grayFrame.copy()
    method = eval('cv.TM_CCOEFF')
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # print(frame_no)
    # print(bottom_right)
    # print(np.amax(res))
    # print("----")

    found_match = False
    if np.amax(res) > 15000000:
        found_match = True
        # print(">>>>>>>> FOUND MATCH <<<<<<<<<")


    if last_frame_found_match is False and found_match is True:
        # print(">>>>>>>> STORING FRAME <<<<<<<<<")
        print(frame_no)
        # cv.rectangle(img,top_left, bottom_right, 255, 2)
        # plt.subplot(121),plt.imshow(res,cmap = 'gray')
        # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122),plt.imshow(img,cmap = 'gray')
        # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        # plt.show()

    last_frame_found_match = found_match
    # define q as the exit button
    if cv.waitKey(25) & 0xFF == ord('q'):
        break




# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv.destroyAllWindows()
