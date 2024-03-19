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
cookie= os.environ.get("COOKIE")
headers = {
    'Host': 'weixin.sogou.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    "cookie":cookie,
}

num_page = 5
other_kwd = ""
for name in ["文劲宇","胡家兵","尤政","张明","李元元","张广军"]:
    for year in ["2023","2024"]:
        query_key = f"{name},{year},{other_kwd}"
        current_time = int(time.time())
        for page_i in range(1,num_page+1):
            file_path = f'{page_folder_path}/{name}-{year}-{other_kwd}{page_i}.html'
            if os.path.exists(file_path):
                continue

            url = f"https://weixin.sogou.com/weixin?ie=utf8&s_from=input&_sug_=y&_sug_type_=&query={query_key}&page={page_i}&type=2&sst0={current_time}"
            print(url)
            response = requests.get(url,headers=headers)
            text = response.text
            open(file_path, 'w', encoding='utf-8').write(text)
            length = len(text)
            print(query_key,page_i,length)
            if length < 10000:
                print("触发反爬检测，休息一下吧")
                os.remove(file_path)
                exit()
            # elif length < 100000:
            #     break
            else:
                time.sleep(random.randint(1,10))


