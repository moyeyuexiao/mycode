import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import cairosvg


img_path=[]
toolimg=[]
def add_alpha_channel(img):
    """ 为jpg图像添加alpha通道 """

    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道

    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道
    return img_new


def merge_img(jpg_img, png_img, y1, y2, x1, x2):
    """ 将png透明图像与jpg图像叠加
        y1,y2,x1,x2为叠加位置坐标值
    """

    # 判断jpg图像是否已经为4通道
    if jpg_img.shape[2] == 3:
        jpg_img = add_alpha_channel(jpg_img)

    '''
    当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
    这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
    '''
    yy1 = 0
    yy2 = png_img.shape[0]
    xx1 = 0
    xx2 = png_img.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > jpg_img.shape[1]:
        xx2 = png_img.shape[1] - (x2 - jpg_img.shape[1])
        x2 = jpg_img.shape[1]
    if y2 > jpg_img.shape[0]:
        yy2 = png_img.shape[0] - (y2 - jpg_img.shape[0])
        y2 = jpg_img.shape[0]

    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_png = png_img[yy1:yy2, xx1:xx2, 3] / 255.0
    alpha_jpg = 1 - alpha_png

    # 开始叠加
    for c in range(0, 3):
        jpg_img[y1:y2, x1:x2, c] = ((alpha_jpg * jpg_img[y1:y2, x1:x2, c]) + (alpha_png * png_img[yy1:yy2, xx1:xx2, c]))

    return jpg_img


def paste(img_jpg_path,img_png_path):
    # 读取图像
    img_jpg = cv2.imread(img_jpg_path, cv2.IMREAD_UNCHANGED)
    img_png = cv2.imread(img_png_path, cv2.IMREAD_UNCHANGED)

    # 设置叠加位置坐标
    x1 = 100
    y1 = 150
    x2 = x1 + img_png.shape[1]
    y2 = y1 + img_png.shape[0]

    # 开始叠加
    res_img = merge_img(img_jpg, img_png, y1, y2, x1, x2)

    # 显示结果图像
    # cv2.imshow('result', res_img)

    # 保存结果图像，读者可自行修改文件路径
    img_p=img_jpg_path.split("/")[2]
    save_path="D:/ans1_img/"+img_p[:-4]+".jpg"
    cv2.imwrite(save_path, res_img)

    # 定义程序退出方式：鼠标点击显示图像的窗口后，按ESC键即可退出程序
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()

def svg_to_jpg():
    for root, dirs, files in os.walk("D:/ans_img"):
        for f in files:
            path="D:/img/"+f[:-4]+".jpg"
            h="D:/img/"+f
            cairosvg.svg2png(file_obj=open(h, "rb"), write_to=path)


def png_to_jpg():
    img = cv2.imread('./ans.png')
    cv2.imwrite("./ans.jpg", img)

def webp_to_png():
    img = cv2.imread('D:/tool_img/an4.webp')
    cv2.imwrite("D:/tool_img/an4.png", img)

def transparent(p):#使透明化
    im = cv2.imread(p)
    height, width, channels = im.shape
    new_im = np.ones((height, width, 4)) * 255
    new_im[:, :, :3] = im
    for i in range(height):
        for j in range(width):
            if new_im[i, j, :3].tolist() == [255.0, 255.0, 255.0]:
                new_im[i, j, :] = np.array([255.0, 255.0, 255.0, 0])
    h, w= im.shape[:2]
    size = (int(w* 0.8), int(h * 0.8))
    new_img = cv2.resize(new_im, size, interpolation=cv2.INTER_AREA)
    path=p[:-4]+".png"
    cv2.imwrite(path, new_img)

def get_img_path_and_tool():
    for root, dirs, files in os.walk("D:/ans_jpg"):
        for f in files:
            h="D:/ans_jpg/"+f
            img_path.append(h)
    for root, dirs, files in os.walk("D:/tool_img"):
        for f in files:
            m="D:/tool_img/"+f
            toolimg.append(m)



if __name__ == '__main__':
    # transparent("D:/tool_img/an4.png")
    get_img_path_and_tool()
    for i in range(len(img_path)):
        if i>1400:
            paste(img_path[i],"D:/tool_img/an4.png")