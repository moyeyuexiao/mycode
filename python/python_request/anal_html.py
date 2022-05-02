import os
from lxml import etree
import sys


if __name__ == '__main__':

    for root, dirs, files in os.walk(r"C:\Users\10449\Desktop\源码获取"):
        for file in files:
            resp = open(os.path.join(root, file), encoding="utf-8").read()
            resp = etree.HTML(resp)
            for i in range(1,9):
                styles = resp.xpath('/html/body/div[1]/div/div/div[2]/div[{}]/div[1]/div/@style'.format(i))[0]
                print(styles.split('"',-1)[1])


