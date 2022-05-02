import re  # 正则
import time  # 代码停顿执行
from selenium import webdriver  # 打开访问的网站
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image  # 图片 安装PIL --> Pillow
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
import os

def wait_img(driver):
    while True:
        time.sleep(0.2)
        resp = driver.page_source
        resp = etree.HTML(resp)
        flag = 1
        now_style = resp.xpath('/html/body/div[1]/div/div/div[2]/div[{}]/div[1]/div/@style'.format(i))
        if "url" not in str(now_style):
            flag = 0
            break
        if flag == 1:
            return True

def translate(content):
    if(content=='traffic lights'):
        return "交通信号灯"
    elif(content=='crosswalks'):
        return "人行横道"
    elif(content=="buses" or content=="bus"):
        return "公交车"
    elif(content=="bicycles"):
        return "自行车"
    elif(content=="a fire hydrant" or content=="fire hydrants"):
        return "消防栓"
    elif(content=="tractors"):
        return "拖拉机"
    elif(content=="motorcycles"):
        return "摩托车"
    elif(content=="stairs"):
        return "楼梯"
    elif(content=="bridges"):
        return "桥"
    elif(content=="chimneys"):
        return "烟囱"
    else:
        return "车辆"



def update(driver):
    obj=driver.find_element_by_xpath('//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div/strong')
    result=translate(obj.text)
    driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", obj, 'id', "hh")
    js="document.getElementById('hh').innerText = '{}'".format(result)
    driver.execute_script(js)
    print(result)
    return result

def driver_main():
    while True:
        try:
            driver = webdriver.Chrome()
            driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
            driver.maximize_window()
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



def circle(driver,a,name):
    time.sleep(5)
    save_path='D:/download/google_img/'+str(a)+'_'+name+'.png'
    driver.save_screenshot(save_path)


if __name__ == '__main__':
    driver=driver_main()
    i=28890
    while i:
        try:
            WebDriverWait(driver, 40, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-reload-button"]')))
            driver.find_element_by_xpath('//*[@id="recaptcha-reload-button"]').click()
            time.sleep(1)
            WebDriverWait(driver, 40, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div/strong')))
            name=update(driver)
            time.sleep(1)
            circle(driver,i,name)
            i+=1
        except Exception as e:
            print(e)
            driver.quit()
            driver = driver_main()

