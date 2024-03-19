import os
from lxml import etree
import pandas as pd
df = pd.DataFrame(columns=["title","keyword","uploader","date","url"])
from datetime import datetime, timedelta

folder_path = os.path.dirname(os.path.realpath(__file__))
page_folder_path = os.path.join(folder_path,'page')

xpath_base = '/html/body/div[1]/main/ol/li'
for root, dirs, files in os.walk(page_folder_path):
    for file in files:
        if file in ['.DS_Store']:
            continue
        keyword = file.split("-")[0]
        filepath =os.path.join(root, file)
        html=open(filepath,"r",encoding="utf-8")\
            .read()\
            .replace("<strong>", "")\
            .replace("</strong>", "")
        tree = etree.HTML(html)
        elements_title = tree.xpath(f"{xpath_base}/h2/a")
        elements_uploader = tree.xpath(f"{xpath_base}/div[1]/a/div[2]/div[1]")
        elements_link = tree.xpath(f"{xpath_base}/div[1]/a/div[2]/div[2]/div/cite")

        for index,element in enumerate(elements_title):
            title = element.text
            uploader = elements_uploader[index].text
            element_time = tree.xpath(f"{xpath_base}[{index+1}]/div[2]/p/span[2]")
            if len(element_time) == 0:
                date = ""
            else:
                date = element_time[0].text
            if date.endswith("ago"):
                datetime_now = datetime.now()
                days_ago = int(date.split()[0])  # 获取x的值
                converted_date = datetime_now - timedelta(days=days_ago)  # 计算与当前日期相对的日期
                date = converted_date.strftime('%b %d, %Y') 

            url = elements_link[index].text
            df.loc[len(df)] = [title, keyword, uploader, date, url]


data_path = os.path.join(folder_path,"data.csv")
df.sort_values(by="date", inplace=True)
df.to_csv(data_path, index=False)

