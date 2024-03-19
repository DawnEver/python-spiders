import os
import re
import requests

folder_path = os.path.dirname(os.path.realpath(__file__))

# parse url
if 1:
    matches_url = []
    url_folder_path = os.path.join(folder_path,'url')
    for root, dirs, files in os.walk(url_folder_path):
        for name in files:
            filepath =os.path.join(root, name)
            input_string=open(filepath,"r",encoding="utf-8").read()
            pattern_url = r'__biz=.*?#rd'
            matches_url += re.findall(pattern_url, input_string)
    url_txt_path = os.path.join(folder_path,"url.txt")
    open(url_txt_path, 'w', encoding='utf-8').write("\n".join(matches_url))


page_folder_path = os.path.join(folder_path,'page')
if not os.path.exists(page_folder_path):
    os.makedirs(page_folder_path)

# get page
for index, m_url in enumerate(matches_url):
    url = r"http://mp.weixin.qq.com/s?"+m_url
    res = requests.get(url)
    filepath = f"{page_folder_path}/{index}.html"
    open(filepath, 'w', encoding='utf-8').write(res.text)
