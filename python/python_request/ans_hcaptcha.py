# -*- coding:utf-8 -*-
# File: ans_find.py
# User: ZLY
# Time: 2021/12/23 16：17
import cv2
import os
import numpy as np
from PIL import Image


def nine(x,y,save_dir,path):
    # 判断九宫格的坐标代表哪块区域
    # save_change(save_dir,哪块区域,x1,y1,x2,y2)
    if x >= 0 and y >= 146 and x <= 160 and y <= 311:
        save_change(save_dir, 1, 0, 146, 160, 311,path)
    elif x >= 161 and y >= 146 and x <= 324 and y <= 311:
        save_change(save_dir, 2, 161, 146, 324, 311,path)
    elif x >= 325 and y >= 146 and x <= 478 and y <= 311:
        save_change(save_dir, 3, 325, 146, 478, 311,path)
    elif x >= 0 and y >= 312 and x <= 160 and y <= 470:
        save_change(save_dir, 4, 0, 312, 160, 470,path)
    elif x >= 161 and y >= 312 and x <= 324 and y <= 470:
        save_change(save_dir, 5, 161, 312, 324, 470,path)
    elif x >= 325 and y >= 312 and x <= 478 and y <= 470:
        save_change(save_dir, 6, 325, 312, 478, 470,path)
    elif x >= 0 and y >= 471 and x <= 160 and y <= 629:
        save_change(save_dir, 7, 0, 471, 160, 629,path)
    elif x >= 161 and y >= 471 and x <= 324 and y <= 629:
        save_change(save_dir, 8, 161, 471, 324, 629,path)
    elif x >= 325 and y >= 471 and x <= 478 and y <= 629:
        save_change(save_dir, 9, 325, 471, 478, 629,path)


def save_change(save_dir, n, x1, y1, x2, y2,path):
    pil_im = Image.open(path)
    box = (x1, y1, x2, y2)
    region = pil_im.crop(box)#切割图片
    out = region.resize((128, 128))
    save_dir = save_dir + str(n) + ".png"
    print(save_dir)
    out.save(save_dir)


if __name__ == '__main__':
    with open("D:/download/hcaptcha.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            path="D:/download/hcaptcha/"+line.split(" ")[0]
            savedir="D:/download/hpatcha_ans/"+line.split(" ")[0]+"_"
            p=line.split(" ")[1]
            point=p.split("|")
            for point in point:
                pointx = int(point.split(",")[0])
                pointy = int(point.split(",")[1])
                nine(pointx, pointy, savedir, path)
    # judge()