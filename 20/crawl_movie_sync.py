import time

import requests
from bs4 import BeautifulSoup


# 在运行之前首先安装lxml，命令 pip3 install lxml
# 否则报错 `couldn't find a tree builder with the features you requested lxml`
def main():
    # 需要设置user-agent，不然获取不到content
    # 参考https://stackoverflow.com/questions/25491872/request-geturl-returns-empty-content
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
    url = "https://movie.douban.com/cinema/later/beijing/"
    page_content = requests.get(url, headers={'User-Agent': user_agent}).content
    page_soup = BeautifulSoup(page_content, "lxml")

    all_movies = page_soup.find("div", id="showing-soon")

    for each_movie in all_movies.find_all("div", class_="item"):
        all_a_tag = each_movie.find_all("a")
        all_li_tag = each_movie.find_all("li")

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]["href"]
        movie_date = all_li_tag[0].text

        response_item_content = requests.get(url_to_fetch, headers={'User-Agent': 'test'}).content
        response_item_soup = BeautifulSoup(response_item_content, "lxml")
        img_tag = response_item_soup.find("img")

        print("{} {} {}".format(movie_name, movie_date, img_tag["src"]))


start_time = time.perf_counter()
main()
print("time spend:", time.perf_counter() - start_time)
