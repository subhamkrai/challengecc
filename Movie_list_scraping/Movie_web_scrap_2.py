import requests
from bs4 import BeautifulSoup
import xlsxwriter


No = []
Name= []
year=[]
rating=[]



URL = "https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')
for items in soup.find('div', class_='lister').find_all('h3', class_='lister-item-header'):	
    
    data_1=(items.find_all('span', class_='lister-item-index'))   
    No.append((data_1[0].text).replace('.',''))
    data_2=(items.find_all('a'))	
    Name.append(data_2[0].text)
    data_3=(items.find_all('span', class_='lister-item-year'))   
    year.append((data_3[0].text).replace('(','').replace(')',''))

for items in soup.find('div', class_='lister').find_all('div', class_='ratings-bar'):
    data_4=(items.find_all('div',class_='inline-block'))
    rating.append((data_4[0].text).replace('\n',''))
    

import pandas
df = pandas.DataFrame(data={'No.': No,'Name': Name,'Year':year,'Rating':rating})
df.to_excel("Movie.xlsx",index=False)


