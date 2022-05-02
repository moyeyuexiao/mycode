from hashlib import md5
import os

def get_list():
    list3=[]
    list1=[]
    count1=[]
    f = open('D:/download/h1.txt','w+',encoding = "UTF-8")
    for path,dir_list,file_list in os.walk("D:/download/Chinese"):
        for file_name in file_list:
            list1.append(os.path.join(path, file_name))
            count1.append(os.path.join(file_name))
    for n in range(len(list1)):
        hash = md5()
        img = open(list1[n], 'rb')
        hash.update(img.read())
        img.close()
        list2 = [count1[n],hash.hexdigest()]
        f.write(str(list2)+'\n')
        list3.append(list2)
    res = []
    f1= open("D:/download/h1.txt",'r',encoding= 'UTF-8')
    for i in f1:
        jpg_str = eval(i[:-1])[0]
        md5_str = eval(i[:-1])[1]
        res.append(md5_str)
    a=len(res)
    print(a)
    res = list(set(res))
    b=len(res)
    print(b)
    print(a-b)



def fgt(a):
    return a


def solve():
    f = open('D:/download/fl_img/hh.txt', 'w+', encoding="UTF-8")
    f.write(str(get_list()))


if __name__ == '__main__':
    get_list()
