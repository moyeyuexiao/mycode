import base64,requests
api_post_url = "http://www.bingtop.com/ocr/upload/"
img_url = r'D:\download\数美+网易\数美\00d2329a14924824a883d27d2be9dcee_秦察者断.jpg'
with open(img_url,'rb') as pic_file:
    img64=base64.b64encode(pic_file.read())
params = {
    "username": "%s" % api_username,
    "password": "%s" % api_password,
    "captchaData": img64,
    "captchaType": 1001
}
response = requests.post(api_post_url, data=params)
dictdata=json.loads(response.text)
# dictdata: {"code":0, "message":"", "data":{"captchaId":"1001-158201918112812","recognition":"RESULT"}}