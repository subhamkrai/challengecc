import requests
from bs4 import BeautifulSoup
import xlsxwriter


title = []
author= []
year=[]
language=[]



URL = "https://en.wikipedia.org/wiki/Le_Monde%27s_100_Books_of_the_Century"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('table', class_='wikitable').find_all('tr')[1:]:
    data=(items.find_all(['th','td']))
    title.append(data[1].text)
    author.append(data[2].text)
    year.append(data[3].text)
    language.append(data[4].text)


import pandas
df = pandas.DataFrame(data={"Title": title, "Author": author, "Year": year, "Language": language})
df.to_excel("Book.xlsx",index=False)



