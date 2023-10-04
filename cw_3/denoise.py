import cv2 as cv
import random

img = cv.imread('ghost1.png',cv.IMREAD_GRAYSCALE)
density_salt = 0.2
density_pepper = 0.2

#Set number of white pixel (salt)
number_of_white_pixel =int(density_salt * (img.shape[0] * img.shape[1]))

#Add salt to the image (white noise)
for i in range(number_of_white_pixel):
    y_coord = random.randint(0, img.shape[0] -1)
    x_coord = random.randint(0, img.shape[1]-1)
    img[y_coord][x_coord]= 255

#set number of black pixel (pepper)
number_of_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

#Add pepper to the image
for i in range(number_of_black_pixel):
    y_coord = random.randint(0, img.shape[0]-1)
    x_coord = random.randint(0, img.shape[1]-1)
    img[y_coord][x_coord]= 0

# Show the image with noise
cv.imshow('denoise_resault_window', img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite('resault_image.png', img)
