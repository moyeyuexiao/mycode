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
import urllib.request

def driver_main():

    while True:
        try:
            driver = webdriver.Chrome()
            driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
            WebDriverWait(driver,40,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/main/form/fieldset/div/div/div/iframe')))
            driver.switch_to.frame(0)
            WebDriverWait(driver,40,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="recaptcha-anchor"]/div[1]')))
            driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]').click()
            driver.switch_to.parent_frame()
            driver.switch_to.frame(2)
            WebDriverWait(driver, 40, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[1]/div/div[1]/img')))
        except Exception as e:
            print(e)
            driver.quit()
        else:
            return driver


def refresh(img_num,driver):
    resp = driver.page_source
    resp = etree.HTML(resp)
    trans(driver)
    name = resp.xpath('//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div/strong/text()')[0]
    print(name)
    # url = resp.xpath('//*[@id="rc-imageselect-target"]/table/tbody/tr[1]/td[1]/div/div[1]/img/@src')[0]
    # f = open(r"D:\download\google_img_expand\{}_{}.jpg".format(img_num,name), 'wb')
    # f.write(urllib.request.urlopen(url).read())
    # f.close()


def trans(driver):
    js = 'return document.getElementByXPATH("//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div/strong")[0].value'
    print(driver.execute_script(js))



if __name__ == '__main__':
    img_num=0
    driver=driver_main()
    refresh(img_num,driver)
    # while img_num:
    #     try:
    #         driver.find_element_by_xpath('//*[@id="recaptcha-reload-button"]').click()
    #         refresh(img_num, driver)
    #     except Exception as e:
    #         print(e)
    #         driver.quit()
    #         driver = driver_main()
    #     img_num+=1
