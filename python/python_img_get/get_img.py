# -*- coding:utf-8 -*-
# File: get_img.py
# User: ZLY
# Time: 2021/10/13 19：37
import os

def rreplace(self, old, new, *max):#倒叙替换字符
    count = len(self)
    if max and str(max[0]).isdigit():
        count = max[0]
    return new.join(self.rsplit(old, count))

def get_():
    dic={}
    ans=[]
    name = {}
    n=1
    for root, dirs, files in os.walk("D:/download/vtt—forlinyu/ans_test"):
        for f in files:
            dic[f[7:-4]]=f
    name_txt = open("D:/voc.names", "w+", encoding="utf-8")
    for root, dirs, files in os.walk("D:/download/vtt—forlinyu/jpgs_test"):
        for fi in files:
            if(fi[8:-4] in dic.keys()):
                ans.append("D:/download/vtt—forlinyu/jpgs_test/")
                ans.append(fi)
                ans.append(" ")
                with open("D:/download/vtt—forlinyu/ans_test/"+dic[fi[8:-4]] , 'r', encoding="UTF-8") as f:
                    for line in f.readlines():
                        if line[0].isdigit():
                            line = line.strip('\n')
                            line = line.replace(" ", ",")
                            line = rreplace(line, ",", "_", 1)
                            temp = line.split(",")
                            name_str = "".join(temp[-1])
                            point = ",".join(temp[0:2])
                            end_x=str(int(temp[2])+int(temp[0]))
                            end_y=str(int(temp[3])+int(temp[1]))
                            ans.append(point)
                            ans.append(",")
                            ans.append(end_x)
                            ans.append(",")
                            ans.append(end_y)
                            print(ans)
                            if name_str not in name:
                                name[name_str] = n
                                ans.append(",")
                                ans.append(n)
                                ans.append(" ")
                                n += 1
                            else:
                                ans.append(",")
                                ans.append(name.get(name_str))
                                ans.append(" ")
                ans.append('\n')

    dataset=open("D:tuwen_train.txt","w+",encoding="utf-8")
    for i in range(len(ans)):#写入tuwen_train.txt
        dataset.write(str(ans[i]))
    name_list=list(name)
    for i in range(len(name_list)):#写入voc.names
        name_txt.write(str(name_list[i]))
        name_txt.write('\n')




if __name__ == '__main__':
    get_()