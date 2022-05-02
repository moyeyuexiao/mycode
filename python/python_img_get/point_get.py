import cv2
import os
import numpy as np
from PIL import Image

final_ans=[]
path="D:/download/shumeivtt/"
dataset = open("D:/shumeiallvtt_train.txt", "w+", encoding="utf-8")

def seperate_mixed():
    L = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:  # 只要jpg文件
            if (os.path.join(root, name)[-4:] == '.jpg'):
                L.append(os.path.join(root, name))
    return L

def get_():
    path_list = seperate_mixed()  # 获取jpg文件列表
    for i in path_list:
        final_ans.append(i)
        find_img(i)
        # if(num!=None):
        #     x,y,w,h=num
        #     final_ans.append(" "+str(x)+","+str(y)+",")
        #     x1=str(int(x)+int(w))
        #     y1=str(int(y)+int(h))
        #     final_ans.append(x1+","+y1+",1 ")
        final_ans.append('\n')
    print(final_ans)
    for i in range(len(final_ans)):  # 写入tuwen_train.txt
        dataset.write(str(final_ans[i]))


def type_get():
    path_list = seperate_mixed()  # 获取jpg文件列表
    for i in path_list:
        num = find_img(i)
        if (num != None):
            img = cv2.imread(i)
            x, y, w, h = num
            cropped=img[y-3:y+h+3,x-3:x+w+3]
            # g = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)  # 灰度化
            path="D:/download/shumei_cut_img/"+i.split("/",-1)[3]
            cv2.imwrite(path,cropped)


def find_img(imgpath):

    img = cv2.imread(imgpath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#灰度化
    ret,binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)#二值化处理
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE  , cv2.CHAIN_APPROX_SIMPLE)

    draw_img3 = cv2.drawContours(img.copy(), contours, -1, (0, 0, 255), 2)

    cv2.imshow("draw_img3", draw_img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    name=imgpath[:-4]
    rang=name.split('_',-1)
    for i in range(0,len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        x1, y1, w1, h1 = cv2.boundingRect(contours[i-1])
        if(x!=0 and y!=0 and x-x1>2):
            final_ans.append(" " + str(x) + "," + str(y) + ",")
            x2 = str(int(x) + int(w))
            y2 = str(int(y) + int(h))
            final_ans.append(x2 + "," + y2 + ",1 ")


def img_watch():
    img = Image.open(r"D:\download\shumeivtt\1156911136937809306_144_45.jpg")
    # img.show()
    img_array = np.array(img)  # 把图像转成数组格式img = np.asarray(image)
    shape = img_array.shape
    print(img_array.shape)
    # for i in range(0, shape[0]):
    #     for j in range(0, shape[1]):
    #         value = img_array[i, j]
            # print("",value)
            # if value[0] != 0:
            #     print("", value)
    height = shape[0]
    width = shape[1]
    dst = np.zeros((height, width, 3))
    for h in range(0, height):
        for w in range(0, width):
            (b, g, r) = img_array[h, w]
            if (b>150 and g>150 and r>150):  # 白色
                img_array[h, w] = (255, 255, 255)
            dst[h, w] = img_array[h, w]
    img2 = Image.fromarray(np.uint8(dst))
    img2.show(img2)
    img2.save("./1.jpg")



if __name__ == '__main__':
    find_img("D:/tool_img/webp.webp")