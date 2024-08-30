import time
import requests  
from bs4 import BeautifulSoup
import re
import openpyxl
import os
import pandas as pd
from fake_useragent import UserAgent

print("当前工作目录:", os.getcwd())


def open_url(url):
    
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    # 发送GET请求
    res = requests.get(url, headers=headers)

    print(f" {url}状态码: {res.status_code}")

    return res


def find_data(res):
    try:

        soup = BeautifulSoup(res.text, "html.parser")
        data = []

        # 楼盘名
        containers = soup.find_all("div", class_="infos")
        if not containers:
            return [], "未找到任何数据"

        for container in containers:
            # 查找楼盘名
            name = container.find("span", class_="items-name").text.strip()
            # 查找价格信息
            price = "N/A"
            parent_div = container.parent
            price_elem = parent_div.find("a", class_="favor-pos")
            if price_elem:
                price_span = price_elem.find("span")
                price = price_span.text.strip() if price_span else "N/A"
            # 查找地址
            address_dd = container.find("a", class_="address")
            area = address_dd.span.text.strip().replace("\n", " ") if address_dd else "N/A"

            # 户型
            huxing_divs = container.find_all("a", class_="huxing")
            huxing = huxing_divs[0].text.strip().replace("\n", " ") if huxing_divs else "N/A"

            # 将提取的数据添加到列表中
            data.append({
                '楼盘名称': name,
                '房价': price,
                '区域': area,
                '户型': huxing
            })
        return data,"数据提取成功"
    except Exception as e:
        return [], f"数据提取失败: {str(e)}"


def main():
    url = 'https://nj.fang.anjuke.com/loupan/'

    all_data = []

    for i in range(1, 25):  # 假设页码从1开始
        page_url = f"{url}all/p{i}"  # 修正分页URL
        print(f"当前页面: {page_url}")
        res = open_url(page_url)
        page_data, status = find_data(res)
        time.sleep(10)
        # 尝试重新调用当前页面10次
        retry_count = 0
        while status != "数据提取成功" and retry_count < 10:
            print("重试:", retry_count + 1)
            res = open_url(page_url)
            time.sleep(15)
            page_data, status = find_data(res)
            retry_count += 1

        if status != "数据提取成功":
            print(status)
            break

        all_data.extend(page_data)

    # 输出表格
    df = pd.DataFrame(all_data)
    df.to_excel('安居客楼盘数据.xlsx', index=False, engine='openpyxl')

    # 输出文本
    with open('fj820.text', 'w', encoding="utf-8") as f:
        for row in all_data:
            f.write(
                f"楼盘名称: {row.get('楼盘名称', 'N/A')}, 房价（元/㎡）: {row.get('房价', 'N/A')}, 区域: {row.get('区域', 'N/A')}, 户型: {row.get('户型', 'N/A')}\n")


if __name__ == "__main__":
    main()
   