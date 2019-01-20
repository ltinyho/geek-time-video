import os
import requests
import json
from config import GCID, GCESS, CID

video_list = []
agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
headers = {
    "Content-Type": "application/json",
    "Referer": "https://time.geekbang.org/course/detail/130-41518",
    "Origin": "https://time.geekbang.org",
    "Host": "time.geekbang.org",
    "User-Agent": agent,
}
data = {
    "cid": str(CID),
    "order": "earliest",
    "prev": 0,
    "sample": True,
    "size": 200,
}
cookies = {
    "GCID": GCID,
    "GCESS": GCESS
}
r = requests.post("https://time.geekbang.org/serv/v1/column/articles", headers=headers, data=json.dumps(data),
                  cookies=cookies)
if r.status_code != 200:
    print("请求失败,请检查登录问题")
    exit(0)

articleList = r.json()["data"]["list"]
fileList = []
for article in articleList:
    title = article.get("article_title")
    video_media_map = article.get("video_media_map")
    if video_media_map:
        url = video_media_map.get("hd").get("url")
        fileList.append([url, title])
        print(url, title)
file = open("./video_list.json", "w")
file.write(json.dumps(fileList))
