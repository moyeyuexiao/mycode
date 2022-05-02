import os
import cv2
# img=cv2.imread("timg.jpg")
# cv2.imshow("before cut",img)
# cv2.waitKey(0)
# img=img[10:650,300:600]  # 第一个范围表示高度 第二个范围表示宽度
# cv2.imshow("after cut",img)
# cv2.imwrite("cutimage",img)
# cv2.waitKey(0)

path_log="D:/download/VTT_data/train_vtt.txt"
point=[]
def handle_txt():
    j = 0
    with open(path_log,"r",encoding="utf-8") as f:
        for line in f.readlines():
            point=line.split(" ",-1)
            for i in range(len(point)):
                j=j+1
                if point[i].startswith('D'):
                    path=point[i]
                    print(path)
                    name=path.split("/",-1)[4]
                elif point[i][0].isdigit():
                    p=point[i].split(",",-1)
                    print(p)
                    x1=int(p[0])
                    x2=int(int(p[2])+int(5))
                    y1=int(p[1])
                    y2=int(p[3])
                    img = cv2.imread(path)
                    img=img[y1:y2,x1:x2]  # 第一个范围表示高度 第二个范围表示宽度
                    savepath="D:/download/vtt_cut_henghui/img_"+str(j)+".jpg"
                    cv2.imwrite(savepath,img)




if __name__ == '__main__':
    handle_txt()

