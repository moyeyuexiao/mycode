# -*- coding:utf-8 -*-
# File: re_get_img.py
# User: ZLY
# Time: 2021/10/18 20：17

import os

path_log="D:/download/齐鲁打码后/re/log.txt"    #log文件存放的路径
path_img="D:/download/齐鲁打码后/re/"
dataset=open("D:/train.txt","w+",encoding="utf-8")
name_t = open("D:/voc.names", "w+", encoding="utf-8")
final=[]
name={}
center_point=[]
name_list=[]




def write_train():
    n=1
    with open(path_log,"r",encoding="utf-8") as f:
        for line in f.readlines():
            final.append(path_img)
            #图片地址
            try:
                final.append(line.split(" ",4)[1])
            except:
                continue
            final.append(" ")
            #坐标
            point_=line.split(" ",4)[4]
            point=point_[1:-2]
            print(point)
            center_point=point.split("|",-1)
            for i in range(len(center_point)):
                p=center_point[i].split(",")
                if(len(p)==2):
                    p1,p2=center_point[i].split(",")
                    if(p1.isdigit() and p2.isdigit()):
                        pointx_left=str(int(p1)-int(55))
                        if(int(pointx_left)<0):
                            pointx_left=str(0)
                        pointy_left=str(int(p2)-int(40))
                        if(int(pointy_left)<0):
                            pointy_left=str(0)
                        pointx_right=str(int(p1)+int(55))
                        pointy_right=str(int(p2)+int(40))
                        final.append(pointx_left+",")
                        final.append(pointy_left+",")
                        final.append(pointx_right + ",")
                        final.append(pointy_right + ",")
                        # 名字编号
                        name_str = line.split("_", 4)[4]
                        name_txt = name_str.split(".")
                        if name_txt[0] not in name:
                            name[name_txt[0]] = n
                            final.append(n)
                            final.append(" ")
                            n += 1
                        else:
                            final.append(name.get(name_txt[0]))
                            final.append(" ")
            final.append("\n")


    for i in range(len(final)):#写入train.txt
        dataset.write(str(final[i]))


    name_list=list(name)
    for i in range(len(name_list)):#写入voc.names
        name_t.write(str(name_list[i]))
        name_t.write('\n')





if __name__ == '__main__':
    write_train()
