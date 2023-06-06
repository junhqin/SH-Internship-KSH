import csv
import requests
import json

# 打开本地csv文件
with open("boss.csv", "r", encoding='gbk') as f:
    # 读取每一行的价格和地址
    reader = csv.reader(f)
    # 创建一个空列表
    data = []
    # 遍历每一行
    for row in reader:
        # 获取价格
        price = row[0]
        # 获取地址
        address = row[1]
        job = row[2]
        company = row[3]
        # 拼接百度地图API的url，替换你的ak
        url = f"http://api.map.baidu.com/geocoding/v3/?address={address}&output=json&ak=mWIQP1AiGugtUa9YUGB37bZBokfSGZgT"
        # 发送请求，获取响应
        response = requests.get(url)
        print(response.text)
        # 解析json数据，获取经纬度
        result = response.json()
        lng = result["result"]["location"]["lng"]
        lat = result["result"]["location"]["lat"]
        # 将地址、经纬度和价格存入列表，以列表的形式
        data.append([company, job, address, lng, lat, price])

# 打开一个新的json文件
with open("经纬度.json", "w", encoding="utf-8") as f:
    # 将列表写入文件中
    json.dump(data, f, ensure_ascii=False, indent=4)
