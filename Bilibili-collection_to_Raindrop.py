import json
from raindropiopy import API, Collection, CollectionRef, Raindrop
import requests

with open("./Raindrop-token.txt","r") as f:
        Raindrop_api = API(f.read())
Bilibili_collection_url = "https://api.bilibili.com/x/v3/fav/resource/list"
Bilibili_collection_del_url = "https://api.bilibili.com/x/v3/fav/resource/batch-del"
with open("./Bilibili-cookie.txt", "r") as f:
    Bilibili_cookie = f.read()


for collection in Collection.get_collections(Raindrop_api):
    if collection.title == "Bilibili 收藏":
        collection_target = collection

Bilibili_collection_id = "1594457495"

while True:
    response = requests.get(
        Bilibili_collection_url,
        params={
            "media_id": Bilibili_collection_id,
            "order": "mtime",
            "ps": 20,
            "keyword": "",
            "platform": "web",
            "order": "mtime",
            "type": 0,
            "tid": 0,
            "pn": 0,
        },
        cookies={"SESSDATA": Bilibili_cookie},
    )
    for i in json.loads(response.text)["data"]["medias"]:
        print(i["title"])
        print("https://www.bilibili.com/video/{}".format(i["bvid"]))
        print(i["cover"])
        # print(i["intro"])
        print("\n\n")

        raindrop = Raindrop.create_link(
            Raindrop_api,
            collection=collection_target,
            link="https://www.bilibili.com/video/{}".format(i["bvid"]),
            title=i["title"],
            excerpt=i["intro"],
            cover=i["cover"],
        )
        print(f"Done, id={raindrop.id}")

        data = {
            "resources": "{}:{}".format(i["id"], i["type"]),
            "media_id": Bilibili_collection_id,
            "platform": "web",
            "csrf": "bcec0a47fd3ee275a1078ba1c502a9b2",
        }

        response = requests.post(
            Bilibili_collection_del_url, data=data, cookies={"SESSDATA": Bilibili_cookie}
        )

        print("del done" + response.text)
