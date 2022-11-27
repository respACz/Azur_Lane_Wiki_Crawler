import requests
from bs4 import BeautifulSoup

#Use request to get web page information
resp=requests.get("https://azurlane.koumakan.jp/wiki/List_of_Ships_by_Image")
resp.encoding='utf-8'

#Parse web page information with beautifulsoup
main_page=BeautifulSoup(resp.text,"html.parser")

#find all div elements that have href information
hreflist=main_page.find_all("div",attrs={"class":"azl-shipcard"})

#Write the href information to the txt file
for div in hreflist:
    href="https://azurlane.koumakan.jp"+div.find("a").get("href")
    f = open( "href.txt", "a")
    f.write(href+"\n")
    f.close()


