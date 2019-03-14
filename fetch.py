# -*- coding: utf-8 -*- 
import requests
import urllib
import json

from collections import defaultdict
from bs4 import BeautifulSoup


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"}

sess = requests.get(url="http://www.51hao.cc/", headers=headers)

content = sess.content
soup = BeautifulSoup(content, 'html.parser')

result = dict()
fkt = soup.select(".fkt")

for i in range(len(fkt)):
    if i == 0:
        continue
    kt = fkt[i]
    province = kt.select(".fkbj a")[0].text
    city_info = dict()
    elm_city = kt.select(".fklk a")
    for elm in elm_city:
        city_name = elm.text
        city_url = elm.attrs["href"]
        city_url = urllib.parse.urljoin(sess.url, city_url)
        print(city_url)

        city_sess = requests.get(city_url, headers=headers)
        city_soup = BeautifulSoup(city_sess.content, 'html.parser')

        menus = city_soup.select(".ab_menu")
        city_phone = defaultdict(list)
        for menu in menus:
            if "联通" in menu.text:
                opertor = "联通"
            elif "移动" in menu.text:
                opertor = "移动"
            elif "电信" in menu.text:
                opertor = "电信"
            city_phone[opertor] += [li.text for li in menu.find_next("ul").find_all("li")]

        city_info[city_name] = city_phone

        result[province] = city_info

with open("phone.json", "w", encoding="utf-8") as fw:
    json.dump(result, fw, ensure_ascii=False)