import time
import requests
from lxml import etree

#open href file
f_href=open("href.txt","r")
info_url_list=f_href.read().splitlines()

#Determine the range based on the href number of the crawl
for i in range(1,678):
    try:
        resp=requests.get(str(info_url_list[i-1]))
        # Parse web information using lxml
        html = etree.HTML(resp.text)
        #Fetch according to the xpath of the required ship data
        names = html.xpath("/html/body/div[3]/h1/text()")
        rarity = html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/table/tbody/tr[2]/td/text()")
        faction = html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/table/tbody/tr[4]/td/a/text()")
        classification = html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/table/tbody/tr[3]/td/a[2]/text()")

        img=html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[1]/div/div[1]/img/@src")
        #Print the ship name for easy viewing and downloading
        print(names[0])
        #Images are stored in the Images folder
        image=open("image/" + names[0] + ".png","wb+")
        url=requests.get(img[0])
        image.write(url.content)
        image.close()
        f = open("data_ship.txt", "a",encoding='utf-8')
        f.write("{\"name\":"+"\""+names[0]+"\""+", \"rarity\":"+"\""+rarity[0].replace("\n","",1).replace("★","",6)+"\""+", \"faction\":"+"\""+faction[0]+"\""+", \"classification\":"+"\""+classification[0]+"\""+"},")
        f.close()
        #The print AC displays that the download is successful
        print("AC")
        #Close the request and set sleep to prevent the site from unconnecting from the host
        resp.close()
        time.sleep(3)
        #Skip web connection errors and errors resulting from xpath mismatches
    except (IndexError,requests.exceptions.ConnectionError):
        #The print WA displays that the download is error
        print("WA")
        pass
    continue