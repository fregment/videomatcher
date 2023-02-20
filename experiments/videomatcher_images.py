import os
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from time import strftime
from time import gmtime

directory = "./frames"

template = cv.imread('template_F01.jpg',0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
#methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR','cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

# Loop until the end of the video
seconds = 0
last_frame_found_match = False
filenames = os.listdir(directory)
sorted_filenames = sorted(filenames, key=lambda x: int(x.split('.')[0]) if x.endswith(".jpg") else 0)

for filename in sorted_filenames:
    if filename.endswith(".jpg"):

        filepath = os.path.join(directory, filename)
        # print(filepath)

        seconds += 1
        # frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0,
        #                      interpolation = cv2.INTER_CUBIC)

        img_frame = cv.imread(filepath,0)
        img = img_frame.copy()

        # grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #
        # img = grayFrame.copy()
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

        # print(second)
        # print(bottom_right)
        # print(np.amax(res))
        # print("----")

        found_match = False
        if np.amax(res) > 15000000:
            found_match = True
            # print(">>>>>>>> FOUND MATCH <<<<<<<<<")


        if last_frame_found_match is False and found_match is True:
            # print(">>>>>>>> STORING FRAME <<<<<<<<<")
            timestamp = strftime("%H:%M:%S", gmtime(seconds))
            print(timestamp)
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
