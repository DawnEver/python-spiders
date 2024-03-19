import requests
import time
import random
import os
from dotenv import load_dotenv
load_dotenv()

folder_path = os.path.dirname(os.path.realpath(__file__))
page_folder_path = os.path.join(folder_path,'page')
if not os.path.exists(page_folder_path):
    os.makedirs(page_folder_path)

url = "https://www.bing.com"
cookie = os.environ.get("COOKIE")
headers = {
    "Host": "www.bing.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-full-version": '"121.0.2277.106"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"10.0.0"',
    "sec-ch-ua-model": '""',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version-list": '"Not A(Brand";v="99.0.0.0", "Microsoft Edge";v="121.0.2277.106", "Chromium";v="121.0.6167.140"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
    "Cookie": cookie,
    "sec-ms-gec-version": "1-121.0.2277.106"
}

num_page = 5

other_kwd = "华中科技大学"
for name in ["文劲宇","胡家兵","尤政","张明","李元元","张广军"]:
    for year in ["2023","2024"]:
        query_key = f"%27{name}%27%26%27{year}%27%26{other_kwd}"
        current_time = int(time.time())
        query_key_byte = query_key# urllib.parse.quote(query_key)
        for page_i in range(num_page):
            file_path = f'{page_folder_path}/{name}-{year}-{other_kwd}-{page_i}.html'
            if os.path.exists(file_path):
                continue
            num = page_i*10+1
            url = f"https://www.bing.com/search?q={query_key_byte}&first={num}"
            print(url)
            response = requests.get(
                url,
                headers=headers
            )
            text = response.text
            open(file_path, 'w', encoding='utf-8').write(text)
            length = len(text)
            print(query_key,page_i,length)
            if length < 80000:
                print("没有搜索到条目，休息一下吧")
                os.remove(file_path)
                exit()
            else:
                time.sleep(random.randint(1,10))


