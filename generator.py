# -*- coding: utf-8 -*- 

import json

with open("phone.json","r",encoding="utf-8") as fr:
    data = json.load(fr)

def fillzero(num, digit=4):
    num = str(num)
    num_len = len(num)
    if num_len < digit:
        return (digit - num_len) * "0" + num
    else:
        return num


province = "广东"
city = "广州"
opertor = "移动"
n = 0
with open("%s-%s-%s.txt"%(province, city, opertor), "w", encoding="utf-8") as fw:
    for p in data[province][city][opertor]:
        n += 1
        for i in range(10000):
            fw.write(p + fillzero(i)+"\n")
        print(p)
print("总:",n*10000,"万条")