import cv2
import numpy as np
import copy
def one():
    img = cv2.imread('D:/tool_img/an4.jpg')
    img2 = copy.deepcopy(img)
    img3 = copy.deepcopy(img)
    img4 = copy.deepcopy(img)
    img5 = copy.deepcopy(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)  # opencv里面画轮廓是根据白色像素来画的，所以反转一下。
    #ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img2, contours, -1, (0, 0, 255), 3)

    area = map(cv2.contourArea, contours)
    area_list = list(area)
    area_max = max(area_list)
    post = area_list.index(area_max)

    cv2.drawContours(img4, contours, post, (0, 0, 255), 3)

    cimg = np.zeros_like(img)
    cimg[:, :, :] = 255

    cv2.drawContours(cimg, contours, post, color=(0, 0, 0), thickness=-1)

    final = cv2.bitwise_or(img5, cimg)

    cv2.imshow('6', final)  # 执行或操作后生成想要的图片
    cv2.waitKey(0)
    cv2.imwrite("D:/tool_img/an4.png",final)

def two():
    im = cv2.imread('D:/tool_img/an7.png')
    height, width, channels = im.shape
    new_im = np.ones((height, width, 4)) * 255
    new_im[:, :, :3] = im
    for i in range(height):
        for j in range(width):
            if new_im[i, j, :3].tolist() == [255.0, 255.0, 255.0]:
                new_im[i, j, :] = np.array([255.0, 255.0, 255.0, 0])
    cv2.imwrite('D:/tool_img/an8.png', new_im)


if __name__ == '__main__':
    one()
