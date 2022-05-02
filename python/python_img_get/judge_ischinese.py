import os

def judge():
    list1=[]
    ans={}
    rate=[]
    name=[]
    list2=[]
    num=0
    g = os.walk(r"D:\download\电影网")
    for path, dir_list, file_list in g:
        for file_name in file_list:
            s=file_name.split("_")[1].split(".")[0]
            if(judge_ischinese(s) and len(s)==4):
                list1.append(s)
    for i in range(len(list1)):
        for char in list1[i]:
            #if(char=='不'):
            #    print(list1[i])
            #num+=1
            if char not in ans:
                ans[char]=1
            else:
                ans[char]+=1

    for key in ans.keys():
        if(key==1):
            print(ans.values())
    #print(num)
    #print(len(list1))
    #print(ans)
    #for key in ans.keys():
    #    list2.append(key)
    #print(list2)
    #f = open("D:/download/rate1.txt", "w", encoding="UTF-8")
    #f.write(str(ans))



def judge_ischinese(str):
    for ch in str:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

if __name__ == '__main__':
    judge()