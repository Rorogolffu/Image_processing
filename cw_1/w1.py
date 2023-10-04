import numpy as np
import cv2
import matplotlib.pyplot as plt

def draw_line(image, start_point, end_point, color=(255, 255, 255), thickness=1):

    image_copy = np.copy(image)

    cv2.line(image_copy, start_point, end_point, color, thickness)

    return image_copy

def convolution(image, kernel):

    conv_image = cv2.filter2D(image, -1, kernel)

    return conv_image


object_image = cv2.imread('optical_mouse.jpg', cv2.IMREAD_GRAYSCALE)


height, width = object_image.shape
line_image = np.zeros((height, width), dtype=np.uint8)


start_point = (50, 50)
end_point = (200, 200)

line_image = draw_line(line_image, start_point, end_point, color=255, thickness=2)


plt.subplot(131), plt.imshow(object_image, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(line_image, cmap='gray')
plt.title('Line Image'), plt.xticks([]), plt.yticks([])


convolved_image = convolution(object_image, line_image)

plt.subplot(133), plt.imshow(convolved_image, cmap='gray')
plt.title('Resault.jpg'), plt.xticks([]), plt.yticks([])

plt.show()
