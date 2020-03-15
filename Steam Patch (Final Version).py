# this one is used for crawling comments of each patch
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://steamcommunity.com/games/578080/announcements/detail/1655506336045918090'

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
browser = webdriver.Chrome('C:/Users/Jstarry/Desktop/chromedriver.exe',chrome_options=options)
#browser = webdriver.Chrome('C:/Users/Lenovo/Desktop/chromedriver.exe',chrome_options=options)

browser.get(url)
browser.implicitly_wait(10)


page = 0

while page < 1472:
    scroll = browser.find_element_by_xpath("//a[contains(@id,'commentthread_ClanAnnouncement_103582791457492425_1655506336045918090_pagebtn_next') and contains(@class,'pagebtn')]")
    scroll.click()
    time.sleep(1)
    page+=1

    review = []
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    for i in soup.find_all('div',{'class':'commentthread_comment_content'}):
        per_review =i.find('div',{'class':'commentthread_comment_text'}).get_text()
        review.append(per_review)


    with open('Update #5.txt','a',encoding = 'utf-8') as f:
        for each in review:
            f.write(each+'\n')
        