import asyncio
import time

import aiohttp

from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
header = {'User-Agent': user_agent}


async def fetch_content(url):
    async with aiohttp.ClientSession(
            headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    page_content = await fetch_content(url)
    page_soup = BeautifulSoup(page_content, "lxml")

    movie_names, urls_to_fetch, movie_dates = [], [], []

    all_movies = page_soup.find("div", id="showing-soon")
    for each_movie in all_movies.find_all("div", class_="item"):
        all_a_tag = each_movie.find_all("a")
        all_li_tag = each_movie.find_all("li")

        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]["href"])
        movie_dates.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in urls_to_fetch]
    pages = await asyncio.gather(*tasks)

    for move_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, "lxml")
        img_tag = soup_item.find("img")

        print("{} {} {}".format(move_name, movie_date, img_tag["src"]))


start_time = time.perf_counter()
asyncio.run(main())
print("time spend:", time.perf_counter() - start_time)
