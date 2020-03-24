import numpy as np
import cv2
from PIL import Image

# Read image

imNDG = Image.open('bolt.jpg').convert('L')
im = np.array(imNDG)


im = cv2.imread('bolt.jpg')
img = np.float32(imNDG)/255


gx = cv2.Sobel(img,cv2.CV_32F,1,0,ksize=1)
gy = cv2.Sobel(img,cv2.CV_32F,0,1,ksize=1)

mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
print("something")


for i in range(0,8):
    for j in range(0,8):
        print(mag[i,j])
print ("Ameeeeeeeeeeeeeeeeeeeeeeeeer")

cv2.imshow("bolt", mag)
cv2.waitKey(0)
cv2.destroyAllWindows()

