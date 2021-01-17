# import the necessary packages
import cv2
 
# load the image and show it
image = cv2.imread("DIP.png")

#Question 1
dim = (image.shape[1]*1, image.shape[0]*1)

# perform the actual resizing of the image and show it
bilinear = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

bicubic = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)

cv2.imwrite("bilinear.png", bilinear)

cv2.imwrite("bicubic.png", bicubic)

#Question 2
dim1 = (int(image.shape[1]*0.2), int(image.shape[0]*0.2))
dim2 = (int(image.shape[1]*3), int(image.shape[0]*3))
dim3 = (int(image.shape[1]*10), int(image.shape[0]*10))

# perform the actual resizing of the image and show it
bilinear1 = cv2.resize(image, dim1, interpolation=cv2.INTER_LINEAR)
bilinear2 = cv2.resize(image, dim2, interpolation=cv2.INTER_LINEAR)
bilinear3 = cv2.resize(image, dim3, interpolation=cv2.INTER_LINEAR)

bicubic1 = cv2.resize(image, dim1, interpolation=cv2.INTER_CUBIC)
bicubic2 = cv2.resize(image, dim2, interpolation=cv2.INTER_CUBIC)
bicubic3 = cv2.resize(image, dim3, interpolation=cv2.INTER_CUBIC)

cv2.imwrite("bilinear 0.2.png", bilinear1)
cv2.imwrite("bilinear 3.0.png", bilinear2)
cv2.imwrite("bilinear 10.0.png", bilinear3)

cv2.imwrite("bicubic 0.2.png", bicubic1)
cv2.imwrite("bicubic 3.0.png", bicubic2)
cv2.imwrite("bicubic 10.0.png", bicubic3)
