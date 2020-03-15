from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.reddit.com/r/battleroyalegames/comments/7ufh1h/pubg_news_battlegrounds_patch_notes_update_4_13118/'

ourUrl=urllib.request.urlopen(url)

soup=BeautifulSoup(ourUrl,'html.parser')

print(soup.prettify())

review=[] 
for i in soup.find_all('div',{'class':'_3h7_WaVl17ooQTHO2Uzr2s s1hmcfrd-0 ckueCN'}):  
    per_review=i.find('p') 
    print(per_review)
    review.append(per_review)

len(review)

New_review=[]
for each in review:
    new_each=str(each)
    new_each=new_each[28:-4]
    print (new_each)
    New_review.append(new_each)

with open('Review4.txt','a',encoding = 'utf-8') as f:
    for each in New_review:
         f.write(each+'\n')