import requests
from Bilibili.Bilibili_Login import bzlogin

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.bilibili.com",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) " "Chrome/83.0.4103.61 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
}

cookie = {"SESSDATA": ""}

cookie["SESSDATA"] = bzlogin()

res = requests.get("https://api.bilibili.com/x/web-interface/nav", headers=headers, cookies=cookie)

print(res)

print(res.json()["data"]["uname"])
