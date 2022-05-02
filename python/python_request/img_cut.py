from PIL import Image
import os
import cv2
import numpy as np
def img_cit(a):
    try:
        img = Image.open(r"D:\download\hca\{}".format(a))
        cropped = img.crop((641, 52,1126, 777))  # (left, upper, right, lower)
        cropped.save(r"D:\download\hcaptcha\{}".format(a))
    except Exception as e:
        print(e)

def img_cut(b):
    try:
        img = Image.open(r"D:\download\hca\{}".format(b))
        cropped = img.crop((849, 52,1336, 777))  # (left, upper, right, lower)
        cropped.save(r"D:\download\hcaptcha\{}".format(b))
    except Exception as e:
        print(e)

def judge(imgpath):
    i=0
    img = cv2.imdecode(np.fromfile(imgpath, dtype=np.uint8), -1)
    #横向判断白色像素点的数量
    for y in range(img.shape[1]):
        if all(img[54,y] == 255):
            i+=1
    if i==502:
        return True
    elif i==501:
        return False

if __name__ == '__main__':
    for home, dirs, files in os.walk(r"D:\download\hca"):
        for filename in files:
            path= "D:/download/hca/" +filename
            if judge(path):
                img_cut(filename)
            else:
                img_cit(filename)



