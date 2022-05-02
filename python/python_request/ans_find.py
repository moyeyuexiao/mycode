# -*- coding:utf-8 -*-
# File: ans_find.py
# User: ZLY
# Time: 2021/12/23 16：17
import cv2
import os
import numpy as np
from PIL import Image

def judge(imgpath):
    img = cv2.imdecode(np.fromfile(imgpath, dtype=np.uint8), -1)
    i=0
    #横向判断白色像素点的数量，十六宫格为74/90，九宫格为79
    for x in range(img.shape[0]):
        if all(img[x,178] == 255):
            i+=1
    print(i)
    if i==98 or i==121:
        return True
    else:
        return False

def sixtenn(x,y,save_dir,path):
    #判断十六宫格的坐标代表哪块区域
    #save_change(save_dir,哪块区域,x1,y1,x2,y2)
    if x>=0 and x<=121 and y>=151 and y<=271:
        save_change(save_dir,1, 0, 151,121, 271,path)
    elif x>=122 and x<=241 and y>=151 and y<=271:
        save_change(save_dir, 2, 122, 151, 241, 271,path)
    elif x>=242 and x<=364 and y>=151 and y<=271:
        save_change(save_dir, 3, 242, 151, 364, 271,path)
    elif x>=365 and y>=151 and x<=485 and y<=271:
        save_change(save_dir, 4, 365, 151, 485, 271,path)
    elif x >= 0 and y >= 272 and x <= 121 and y <= 392:
        save_change(save_dir, 5, 0, 272, 121, 392,path)
    elif x >= 122 and y >= 272 and x <= 241 and y <= 392:
        save_change(save_dir, 6, 122, 272, 241, 392,path)
    elif x >= 242 and y >= 272 and x <= 364 and y <= 392:
        save_change(save_dir, 7, 242, 272, 364, 392,path)
    elif x >= 365 and y >= 272 and x <= 485 and y <= 392:
        save_change(save_dir, 8, 365, 272, 485, 392,path)
    elif x >= 0 and y >= 393 and x <= 121 and y <= 514:
        save_change(save_dir, 9, 0, 393,121, 514,path)
    elif x >= 122 and y >= 393 and x <= 241 and y <= 514:
        save_change(save_dir, 10, 122, 393, 241, 514,path)
    elif x >= 242 and y >= 393 and x <= 364 and y <= 514:
        save_change(save_dir, 11, 242, 393, 364, 514,path)
    elif x >= 365 and y >= 393 and x <= 485 and y <= 514:
        save_change(save_dir, 12, 365, 393, 485, 514,path)
    elif x >= 0 and y >= 515 and x <= 121 and y <= 636:
        save_change(save_dir, 13, 0, 515, 121, 636,path)
    elif x >= 122 and y >= 515 and x <= 241 and y <= 636:
        save_change(save_dir, 14, 122, 515, 241, 636,path)
    elif x >= 242 and y >= 515 and x <= 364 and y <= 636:
        save_change(save_dir, 15, 242, 515, 364, 636,path)
    elif x >= 365 and y >= 515 and x <= 485 and y <= 636:
        save_change(save_dir, 16, 365, 515, 485, 636,path)



def nine(x,y,save_dir,path):
    # 判断九宫格的坐标代表哪块区域
    # save_change(save_dir,哪块区域,x1,y1,x2,y2)
    if x >= 0 and y >= 150 and x <= 159 and y <= 308:
        save_change(save_dir, 1, 0, 150, 159, 308,path)
    elif x >= 159 and y >= 150 and x <= 323 and y <= 308:
        save_change(save_dir, 2, 159, 150, 323, 308,path)
    elif x >= 324 and y >= 150 and x <= 487 and y <= 308:
        save_change(save_dir, 3, 324, 150, 487, 308,path)
    elif x >= 0 and y >= 309 and x <= 159 and y <= 475:
        save_change(save_dir, 4, 0, 309, 159, 475,path)
    elif x >= 159 and y >= 309 and x <= 323 and y <= 475:
        save_change(save_dir, 5, 159, 309, 323, 475,path)
    elif x >= 324 and y >= 309 and x <= 487 and y <= 475:
        save_change(save_dir, 6, 324, 309, 487, 475,path)
    elif x >= 0 and y >= 476 and x <= 159 and y <= 638:
        save_change(save_dir, 7, 0, 476, 159, 638,path)
    elif x >= 159 and y >= 476 and x <= 323 and y <= 638:
        save_change(save_dir, 8, 159, 476, 323, 638,path)
    elif x >= 324 and y >= 476 and x <= 487 and y <= 638:
        save_change(save_dir, 9, 324, 476, 487, 638,path)


def save_change(save_dir, n, x1, y1, x2, y2,path):
    pil_im = Image.open(path)
    box = (x1, y1, x2, y2)
    region = pil_im.crop(box)#切割图片
    out = region.resize((128, 128))
    save_dir = save_dir + str(n) + ".png"
    # print(save_dir)
    out.save(save_dir)


if __name__ == '__main__':
    with open("D:/download/google_img.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            path="D:/download/google_img/"+line.split(" ")[0]
            savedir="D:/download/google_ans/"+line.split(" ")[0][:-4]+"_"
            p=line.split(" ")[1]
            point=p.split("|")
            for point in point:
                pointx = int(point.split(",")[0])
                pointy = int(point.split(",")[1])
                print(path)
                if(judge(path)):
                    sixtenn(pointx, pointy, savedir, path)
                else:
                    nine(pointx, pointy, savedir, path)
    # judge()