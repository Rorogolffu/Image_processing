import cv2 as cv
import numpy as np


# change it with your absolute path for the image
image = cv.imread("./input_img.png")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5, 5),
					cv.BORDER_DEFAULT)
ret, thresh = cv.threshold(blur, 200, 255,
						cv.THRESH_BINARY_INV)

cv.imwrite("1_thresh_res.png",thresh)

contours, hierarchies = cv.findContours(
	thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(thresh.shape[:2],
				dtype='uint8')

cv.drawContours(blank, contours, -1,
				(255, 0, 0), 1)

cv.imwrite("2_contours_res.png", blank)

#blank
blank = cv.copyMakeBorder(blank, 200, 200, 200, 200, cv.BORDER_CONSTANT, None, value = 0)


#blank ---> blank_output
blank_output=blank
img_h,img_w = blank.shape

circle_stamp = np.zeros((100,100),dtype="uint8")
circle_stamp = cv.circle(circle_stamp, (50,50), 29, 10, 2)## ตัว stamp # radian color thick


for y in range(0,img_h):
    for x in range(0,img_w):
        if blank[y,x] > 200:
            # draw stamp

            #detect boader
            if blank_output[y-50:y+50,x-50:x+50].shape != (100,100):
                break
            blank_output[y-50:y+50,x-50:x+50] += circle_stamp[0:100,0:100]

cv.imwrite("3_center_res.png",blank_output)
