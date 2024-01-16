# -*- coding: utf-8 -*-
from qrcode.main import QRCode
import requests
from urllib.parse import urlparse

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.bilibili.com",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) " "Chrome/83.0.4103.61 Safari/537.36",
    "cookie": "",
    "Referer": "https://www.bilibili.com/",
}

headers_login = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Host": "passport.Bilibili.com",
    "Referer": "https://passport.bilibili.com/login",
}


def bzlogin():
    getlogin = requests.get("https://passport.bilibili.com/x/passport-login/web/qrcode/generate", headers=headers_login).json()
    loginurl = getlogin["data"]["url"]
    qrcode_key = getlogin["data"]["qrcode_key"]
    print(qrcode_key)
    qr = QRCode()
    qr.add_data(loginurl)
    img = qr.make_image()
    img.show()
    tokenurl = "https://passport.bilibili.com/x/passport-login/web/qrcode/poll?qrcode_key={}".format(qrcode_key)
    qrcodedata = requests.get(tokenurl, headers=headers_login).json()
    match qrcodedata["data"]["code"]:
        case 0:
            sessdata = [i for i in str(urlparse(qrcodedata["data"]["url"]).query).split("&") if i.startswith("SESSDATA")][0].split("=")[1]
            return sessdata
        case _:
            print(qrcodedata["data"]["message"])
            return None
