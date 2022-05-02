# coding=utf-8
import base64
import json
import requests
import os
from multiprocessing import Pool
import datetime
import random

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

def get_result(path):
    while True:
        try:
            result=base64_api(uname='wjm', pwd='qwe123456', img=path, typeid=22)
            if result[0].isdigit():
                return result
        except Exception as e:
            print(e)
if __name__ == "__main__":
    flag=0
    for home, dirs, files in os.walk(r"D:/download/google_img"):
        for f in files:
            if f=="25057_人行横道.png":
                flag=1
                continue
            if flag==1:
                path="D:/download/google_img/"+f
                result=get_result(path)
                print(path[23:] + " " + result)
                with open("D:/download/google_img.txt", "a+", encoding="utf-8") as f:
                    f.write(path[23:] + " " + result + "\n")
    #     pool.apply_async(get_result,[path,])
    # pool.close()
    # pool.join()
