import requests
import time
import random
import os
from dotenv import load_dotenv
load_dotenv()

folder_path = os.path.dirname(os.path.realpath(__file__))
url_folder_path = os.path.join(folder_path,'url')
if not os.path.exists(url_folder_path):
    os.makedirs(url_folder_path)

# while True:
begin = 300
count = 10
end = 1000

cookie= os.environ.get("COOKIE")
for i in range(begin, end, count):
    url = f'https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&search_field=null&begin={i}&count={count}&query=&fakeid=MjM5MDAyMzM4MA%3D%3D&type=101_1&free_publish_type=1&sub_action=list_ex&token=1982323120&lang=zh_CN&f=json&ajax=1'
    timestamp = int(time.time())
    referer = f'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=77&createType=0&token=1982323120&lang=zh_CN&timestamp={timestamp}'

    headers = {
        'Host': 'mp.weixin.qq.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': referer,
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Cookie': cookie
    }
    response = requests.get(url, headers=headers)
    filename = f'{url_folder_path}/hust{i}-{i+count}.json'
    text = response.text
    open(filename, 'w', encoding='utf-8').write(text)
    if len(text) < 1000:
        print("The spider may be blocked!\nTry to update referer and cookie in headers.")
        break
    time.sleep(random.randint(1,10))
