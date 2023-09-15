import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2023"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "ih-td-tab auction-tbl")
title = table.find_all("th")
header = []
for _ in title:
    name = _.text
    header.append(name)

df = pd.DataFrame(columns = header)

rows = table.find_all("tr")

for _ in rows[1:]:
    first_td = _.find_all("td")[0].find("div", class_ = "ih-pt-ic").text.strip()
    data = _.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0, first_td)
    l = len(df)
    df.loc[l] = row
    
df.to_csv("ipl_Auction_Stats_2023.csv")
