import time
import requests
from lxml import etree

# open href file
f_href=open("href.txt","r")
info_url_list=f_href.read().splitlines()

# Determine the range based on the href number of the crawl
for i in range(1,678):
    try:
        resp=requests.get(str(info_url_list[i-1]))
        # Parse web information using lxml
        html = etree.HTML(resp.text)
        #Fetch according to the xpath of the required ship data
        english_names = html.xpath("/html/body/div[3]/h1/text()")
        rarity = html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/table/tbody/tr[2]/td/text()")
        faction = html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/table/tbody/tr[4]/td/a/text()")
        classification = html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/table/tbody/tr[3]/td/a[2]/text()")
        classes =html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/table/tbody/tr[5]/td[2]/a/text()")
        skill_name=html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/b/text()")


        img_href=html.xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[1]/div/div[1]/img/@src")
        #Print the ship name for easy viewing and downloading
        print(english_names[0])
        # print(english_names[0] + rarity[0]+faction[0]+classification[0])
        # print(classes[0]+skill_name[0])
        print(img_href[0])
        # print(icon_href[0])
        f = open("ship_datas_v1_1.txt", "a",encoding='utf-8')
        f.write("{\"name\":"+"\""+english_names[0]+"\""+", \"rarity\":"+"\""+rarity[0].replace("\n","",1).replace(" ","",1).replace("★","",6)+"\""+", \"faction\":"+"\""+faction[0]+"\""+", \"classification\":"+"\""+classification[0]+"\""+", \"class\":"+"\""+classes[0]+"\"")
        f.write(", \"img_href\":"+"\""+img_href[0]+"\"")
        f.write(", \"skill_name\":"+"\""+skill_name[0]+"\""+"},")
        f.close()
        #The print AC displays that the download is successful
        print("AC")
        #Close the request and set sleep to prevent the site from unconnecting from the host
        resp.close()
        time.sleep(0.5)
        #Skip web connection errors and errors resulting from xpath mismatches
    except (IndexError,requests.exceptions.ConnectionError):
        #The print WA displays that the download is error
        print("WA")
        pass
    continue
# ship_datas_v1_1
