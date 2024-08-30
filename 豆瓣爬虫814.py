import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd
print("当前工作目录:", os.getcwd())


def open_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    print(f"Response status for {url}: {res.status_code}")
    return res


def findmovies(res):
    soup = BeautifulSoup(res.text, "html.parser")
    movies = []
    #提取名称
    targets = soup.find_all("div", class_="hd")
    for each in targets:
        movie_name = each.a.span.text
        bd_div = each.find_next_sibling("div", class_="bd") # find_next_sibling方法查找hd元素的下一个兄弟元素
        #提取评分
        try:
            rating1= bd_div.find("span", class_="rating_num")
            rating=rating1.text
        except AttributeError:
            rating = "N/A"  # 如果找不到评分，则设为N/A
        #提取其他信息
        try: 
            infom = bd_div.p.text.strip().replace("\n", " ")

        except AttributeError:
            infom = "N/A"  # 如果找不到评分，则设为N/A

    
        movies.append({
            '电影名称': movie_name,
            '评分': rating,
            '资料': infom
        })
    return movies


def find_depth(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    # 尝试找到具有类名 'next' 的 span 元素
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling.text
    return int(depth)


def main():
    url = 'https://movie.douban.com/top250'
    host = url
    res = open_url(host)
    depth = find_depth(res)
    print(f"Total pages: {depth}")
    all_movies = []

    for i in range(depth):
        page_url = f"{host}/?start={25 * i}"
        print(f"Fetching page: {page_url}")
        res = open_url(page_url)
        movies = findmovies(res)
        all_movies.extend(movies)



    df = pd.DataFrame(all_movies)
    df.to_excel('电影数据1.xlsx', index=False, engine='openpyxl')


if __name__ == "__main__":
    main()
