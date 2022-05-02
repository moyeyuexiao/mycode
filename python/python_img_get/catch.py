import requests
from lxml import etree
headers={'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.49'}
html=requests.get('https://book.douban.com/top250',headers=headers)
html.text[:200]
print(html.text)
# bs = etree.xpath(html.text)
# bs.xpath('//tr[@class = "item"]/td[2]/p')[0].text
# first_bs=bs.xpath('//tr[@class = "item"]')[0]
# result=first_bs.xpath('td[2]/div[1]/a[1]/@title')