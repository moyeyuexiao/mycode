import cv2
img = cv2.imread(f)
path="D:/img/"+f
cv2.imwrite(path, img)