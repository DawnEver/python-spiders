import os
import re
import pandas as pd
df = pd.DataFrame(columns=["title", "date", "has_seee","url"])

folder_path = os.path.dirname(os.path.realpath(__file__))
page_folder_path = os.path.join(folder_path,'page')

for root, dirs, files in os.walk(page_folder_path):
    for name in files:
        if name in ['.DS_Store']:
            continue
        filepath =os.path.join(root, name)
        text=open(filepath,"r",encoding="utf-8").read()
        # get title
        title_pattern = r'<meta property="og:title" content="([^"]*)"'
        match = re.search(title_pattern, text)
        if match:
            extracted_title = match.group(1)
        else:
            extracted_title = ""
        # get time
        date_pattern = r'\d{4}-\d{2}-\d{2}'
        match = re.search(date_pattern, text)
        if match:
            extracted_date = match.group()
        else:
            extracted_date = ""
        #get url
        url_pattern = r'<meta property="og:url" content="([^"]*)"'
        match = re.search(url_pattern, text)
        if match:
            extracted_url = match.group(1)
        else:
            extracted_url = ""
        # include "电气"
        pattern = "电气"
        if re.search(pattern, text):
            has_seee = True
        else:
            has_seee = False
        df.loc[len(df)] = [extracted_title, extracted_date, has_seee,extracted_url]

data_path = os.path.join(folder_path,"data.csv")
data_seee_path = os.path.join(folder_path,"data_seee.csv")
df.sort_values(by="date", inplace=True)
df.to_csv(data_path, index=False)
df[df["has_seee"]].to_csv(data_seee_path, index=False)

