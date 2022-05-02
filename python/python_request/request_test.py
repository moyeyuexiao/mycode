from selenium import webdriver
import time
from lxml import etree
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import os
import requests

def try_get(url):
    while True:
        try:
            resp = requests.request("get", url, timeout = 3)
        except Exception as e:
            print(e)
        else:
            return resp.content

def get_img(resp,title,page_num):
    resp = etree.HTML(resp)
    for i in range(1,10):
        styles = resp.xpath('/html/body/div[1]/div/div/div[2]/div[{}]/div[1]/div/@style'.format(i))[0]
        img_url = styles.split('"',-1)[1]
        img_response = try_get(img_url)
        with open(r"D:\download\google_img\{}_{}.jpg".format(page_num,title),"wb") as f:
            f.write(img_response)
        page_num+=1
    return page_num


def driver_main():

    driver = webdriver.Chrome()
    driver.get("http://democaptcha.com/demo-form-eng/hcaptcha.html")
    WebDriverWait(driver,40,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/main/article/div/form/div/iframe')))
    driver.switch_to.frame(0)
    WebDriverWait(driver,40,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div[1]')))
    driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div/div[1]').click()
    driver.switch_to.parent_frame()
    WebDriverWait(driver,40,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[1]/iframe')))
    driver.switch_to.frame(1)
    WebDriverWait(driver, 40, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]')))
    return driver


def wait_img(driver):
    while True:
        time.sleep(0.2)
        resp = driver.page_source
        resp = etree.HTML(resp)

        flag = 1
        for i in range(1,10):
            now_style = resp.xpath('/html/body/div[1]/div/div/div[2]/div[{}]/div[1]/div/@style'.format(i))
            if "url" not in str(now_style):
                flag = 0
                break
        title = resp.xpath('/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[1]/text()')[0][7:-3]
        if flag == 1:
            return title


if __name__ == '__main__':
    page_num = 1074
    driver = driver_main()
    while page_num:
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div[7]').click()
            title = wait_img(driver)
            page_num=get_img(driver.page_source,title,page_num)
        except Exception as e:
            print(e)
            driver.quit()
            driver = driver_main()



