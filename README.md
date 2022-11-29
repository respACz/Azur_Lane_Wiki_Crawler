# Azur_Lane_Wiki_Crawler

### 需求**Azur_Lane_Wiki获取碧蓝航线舰娘基础数据和icon图片**

- **Azur_Lane_Wiki_Crawler**
- **fleets’ info & icon image**
- **碧蓝航线Wiki爬虫**
- **舰娘基础信息 & 图片**
- **source website：[https://azurlane.koumakan.jp/wiki/Azur_Lane_Wiki](https://azurlane.koumakan.jp/wiki/Azur_Lane_Wiki)**

### 仓库文件说明，Repository Document Description

- /image : 存放舰娘图片，Store the pictures of the ship
- data_ship.txt : 舰娘基础数据（json格式），Basic data (json format)
- href.txt : 舰娘详细信息页面连接， Ship details page href
- ship_info_href.py : “舰娘详细信息页面连接”的爬虫， the crawler of “Ship details page href”
- ship_datas.py : “舰娘数据和图片”的爬虫，可以下载icon图片，the crawler of “Ship info & icon image”
- ship_datas_v1_1.py : “舰娘详细数据和icon图片链接”的爬虫，the crawler of “Ship derail info & href of icon image”
