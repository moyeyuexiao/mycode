# -*- coding:utf-8 -*-
# File: get_img.py
# User: ZLY
# Time: 2021/10/21 19：11


import os

# path1="D:/download/顶象VTT验证码/"
path2="D:/download/数美VTT验证码/"

log=[]
final_ans=[]
point=[]
# dataset1=open("D:/train_dingxiang.txt","w+",encoding="utf-8")
dataset2=open("D:/train_shumei.txt","w+",encoding="utf-8")


def img_get():
    path=path2+"log.txt"
    with open(path,"r",encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip('\n')
            log=line.split(' ',-1)
            final_ans.append(path2)
            try:
                final_ans.append(log[1])
            except:
                continue
            final_ans.append(" ")
            point=log[1][:-4].split('_')
            pointx_left = str(int(point[1]) - int(22))
            if (int(pointx_left) < 0):
                pointx_left = str(0)
            pointy_left = str(int(point[2]) - int(14))
            if (int(pointy_left) < 0):
                pointy_left = str(0)
            pointx_right = str(int(point[1]) + int(30))
            pointy_right = str(int(point[2]) + int(30))
            final_ans.append(pointx_left + ",")
            final_ans.append(pointy_left + ",")
            final_ans.append(pointx_right + ",")
            final_ans.append(pointy_right + ",")
            final_ans.append("1 ")
            final_ans.append('\n')
    print(final_ans)


    for i in range(len(final_ans)):#写入train_.txt
        dataset2.write(str(final_ans[i]))



if __name__ == '__main__':
    img_get()
