from selenium import webdriver  # 打开访问的网站
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import base64
import json
import requests
from selenium.webdriver.common.action_chains import ActionChains


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


def driver_mian():
    driver=webdriver.Chrome()
    driver.get("http://www.80599.net/")
    driver.maximize_window()
    WebDriverWait(driver, 80, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="broadcast"]/div[2]/div[2]/span[2]/a')))
    return driver


def circle(driver):
    driver.find_element_by_xpath('//*[@id="broadcast"]/div[2]/div[2]/span[2]/a').click()
    driver.switch_to.window(driver.window_handles[-1])

    while True:

        time.sleep(2)
        save_path = "./1.png"
        driver.save_screenshot(save_path)
        try:
            result = base64_api(uname='wjm', pwd='qwe123456', img=save_path, typeid=27)
            point = result.split("|", -1)
            for point in point:
                pointx = int(point.split(",", -1)[0])
                pointy = int(point.split(",", -1)[1])
                ActionChains(driver).move_by_offset(pointx, pointy).click().perform()
                ActionChains(driver).move_by_offset(-pointx, -pointy).perform()
        except Exception as e:
            print(e)
            print("调用验证码接口识别，关闭浏览器后重试")
            break
        else:
            time.sleep(2)
            try:
                WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clicaptcha-container"]/div[2]')))
                print("验证码识别失败，刷新后重试")
                driver.find_element_by_xpath('//*[@id="clicaptcha-container"]/div[3]/a').click()
                time.sleep(2)
            except Exception as e:
                print("验证码通过")
                try:
                    WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/h1/div')))
                    curl = driver.current_url
                    handel_str(curl)
                    break
                except Exception as e:
                    print(e)
                    break
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)

def handel_str(curl):
    sid=curl.split("&")
    for sid in sid:
        if "SID=" in sid:
            print(sid)
            with open("./sid.txt", "a+", encoding="utf-8") as f:
                f.write(sid[4:] + '\n')


if __name__ == '__main__':
    driver=driver_mian()
    for i in range(500):
        circle(driver)

