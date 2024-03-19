import os
from lxml import etree
import pandas as pd
df = pd.DataFrame(columns=["title","keyword","uploader","date","url"])
import re
from datetime import datetime

folder_path = os.path.dirname(os.path.realpath(__file__))
page_folder_path = os.path.join(folder_path,'page')

xpath_base = '/html/body/div[2]/div[1]/div[3]/ul/li/div[2]'
for root, dirs, files in os.walk(page_folder_path):
    for file in files:
        if file in ['.DS_Store']:
            continue
        keyword = file.split("-")[0]
        filepath =os.path.join(root, file)
        html=open(filepath,"r",encoding="utf-8")\
            .read()\
            .replace("<em><!--red_beg-->", "")\
            .replace("<!--red_end--></em>", "")
        tree = etree.HTML(html)
        elements_title = tree.xpath(f"{xpath_base}/h3/a")
        elements_uploader = tree.xpath(f"{xpath_base}/div/span[1]")
        elements_time = tree.xpath(f"{xpath_base}/div/span[2]/script")
        for index,element in enumerate(elements_title):
            title = element.text
            uploader = elements_uploader[index].text
            date_script = elements_time[index].text
            # 使用正则表达式提取时间戳
            timestamp = re.search(r"timeConvert\('(\d+)'\)", date_script).group(1)
            # 将时间戳转换为时间
            date = datetime.fromtimestamp(int(timestamp))
            url = 'https://weixin.sogou.com/'+element.attrib['href']
            df.loc[len(df)] = [title, keyword, uploader, date, url]


data_path = os.path.join(folder_path,"data.csv")
df.sort_values(by="date", inplace=True)
df.to_csv(data_path, index=False)

