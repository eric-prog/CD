import cv2 as cv
import numpy as np

lower = np.array([0, 0, 225])
upper = np.array([255,255,255])

og_img = cv.imread("assets/land_with_clouds.jpeg")

temp_img = cv.cvtColor(og_img, cv.COLOR_BGR2HSV)
mask = cv.inRange(temp_img, lower, upper)
output = cv.bitwise_and(og_img, og_img, mask=mask)

horizontal_view = np.concatenate((og_img, output), axis=1)
cv.imshow('Cloud Detection', horizontal_view)

cv.waitKey(0)
cv.destroyAllWindows()