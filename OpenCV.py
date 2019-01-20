"""
# Image Detection
"""

import cv2
import numpy as np

# Image Detection
img_bgr = cv2.imread("opencv-template-matching-python-tutorial.jpg")
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread("opencv-template-for-matching.jpg", 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshhold = 0.8
loc = np.where(res >= threshhold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)

cv2.imshow('detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
# Image Detection
"""

"""
OpenCV:
How to get specific frame:
https://stackoverflow.com/questions/33523751/getting-specific-frames-from-videocapture-opencv-in-python 


OpenCV:
Open Image
Crop Image
Draw:
Rectangle: cv2.rectangle(streaming, (0, 0), (540, 960), (0, 0, 255), 1) # RED - Frame WeChat Visible border - Correct
Line: cv2.line(streaming, (539, 0), (539, 960), (0,0,255), 1) # RED Rigth Line
Как найти размеры img, работает как с img так и с numpy array:
h, w, c = ground_source_frame.shape 
print(w)
Вырезание img
# frame = source_frame[TOP:BUTTOM, LEFT:RIGHT]
ground_source_frame = frame[5:1080, 407:1173]
"""