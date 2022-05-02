import re  # 正则
import time  # 代码停顿执行
from selenium import webdriver  # 打开访问的网站
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree
import requests
import socket
from selenium.webdriver.chrome.options import Options
import time
from jsonpath import jsonpath
import json
import os
import random
import sys
import requests
import linecache
from lxml import etree
from json import loads
import string
import zipfile

# 用于selenium的添加代理插件
def create_proxyauth_extension(proxy_host, proxy_port,
                               proxy_username, proxy_password,
                               scheme='http', plugin_path=None):
    """代理认证插件

    args:
        proxy_host (str): 你的代理地址或者域名（str类型）
        proxy_port (int): 代理端口号（int类型）
        proxy_username (str):用户名（字符串）
        proxy_password (str): 密码 （字符串）
    kwargs:
        scheme (str): 代理方式 默认http
        plugin_path (str): 扩展的绝对路径

    return str -> plugin_path
    """

    if plugin_path is None:
        plugin_path = 'vimm_chrome_proxyauth_plugin.zip'

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = string.Template(
        """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "${scheme}",
                host: "${host}",
                port: parseInt(${port})
              },
              bypassList: ["foobar.com"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "${username}",
                password: "${password}"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path


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
        if flag == 1:
            return True

def driver_main():
    while True:
        try:
            proxyauth_plugin_path = create_proxyauth_extension(
                proxy_host='tps104.kdlapi.com',
                proxy_port=15818,
                proxy_username='t13862733062369',
                proxy_password='ptysoxw2',
            )
            Chrome_options = webdriver.ChromeOptions()
            Chrome_options.add_extension(proxyauth_plugin_path)
            driver = webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe",
                                      chrome_options=Chrome_options)
            driver.get("http://democaptcha.com/demo-form-eng/hcaptcha.html")
            driver.maximize_window()
            WebDriverWait(driver,40,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/main/article/div/form/div/iframe')))
            driver.switch_to.frame(0)
            WebDriverWait(driver, 40, 5).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div[1]')))
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/div/div/div[1]"))).click()
            driver.switch_to.parent_frame()
            WebDriverWait(driver, 40, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/iframe')))
            driver.switch_to.frame(1)
            WebDriverWait(driver, 40, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]')))
        except Exception as e:
            print(e)
            driver.quit()
        else:
            return driver

def wait_img(driver):
    j=0
    while True:
        j+=1
        time.sleep(0.2)
        resp = driver.page_source
        resp = etree.HTML(resp)
        flag = 1
        for i in range(1,10):
            now_style = resp.xpath('/html/body/div[1]/div/div/div[2]/div[{}]/div[1]/div/@style'.format(i))
            if "url" not in str(now_style):
                flag = 0
                break
        if j>20:
            flag=1
        if flag == 1:
            return True



def circle(driver,a):
    time.sleep(7)
    try:
        name=driver.find_element_by_xpath('html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[1]').text
        save_path='D:/download/hca/'+str(a)+'_'+name[7:-3]+'.png'
        driver.save_screenshot(save_path)
        time.sleep(1)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    driver=driver_main()
    i = 30370
    while i:
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[7]"))).click()
            wait_img(driver)
            circle(driver,i)
            i=i+1
        except Exception as e:
            print(e)
            driver.quit()
            driver = driver_main()

