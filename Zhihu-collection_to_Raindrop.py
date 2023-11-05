# 此脚本需要用户将收藏夹设为公开可见

import requests
from raindropiopy import API, Collection, Raindrop


def get_total(id: int):
    url = "https://www.zhihu.com/api/v4/collections/{id}/items".format(id=id)
    res = requests.get(url).json()
    return res["paging"]["totals"]


def save_collection(Raindrop_api, collection_target, title: str, link: str, excerpt: str, cover: str):
    raindrop = Raindrop.create_link(
        Raindrop_api,
        collection=collection_target,
        link=link,
        title=title,
        excerpt=excerpt,
        cover=cover,
    )
    print(f"Done, id={raindrop.id}")


def get_singleinfo(Raindrop_api, collection_target, id: int, total: int):
    limit = 0
    tmp = ""
    for i in range(limit, total):
        print("Current: {}".format(i))
        try:
            url = "https://www.zhihu.com/api/v4/collections/{id}/items?offset={offset}&limit=1".format(id=id, offset=i)
            res = requests.get(url).json()["data"][0]["content"]
            if res["url"] != tmp:
                tmp = res["url"]
                if "question" in res.keys():
                    save_collection(Raindrop_api, collection_target, res["question"]["title"], res["url"], res["excerpt"], "")
                else:
                    if "title" in res.keys():
                        if "image_url" in res.keys():
                            save_collection(Raindrop_api, collection_target, res["title"], res["url"], res["excerpt_title"], res["image_url"])
                        else:
                            save_collection(Raindrop_api, collection_target, res["title"], res["url"], res["excerpt_title"], "")
                    else:
                        save_collection(
                            Raindrop_api,
                            collection_target,
                            res["excerpt_title"],
                            res["url"],
                            res["content"][0]["own_text"],
                            res["content"][1]["cropped_url"],
                        )
            else:
                continue
        except:
            print("Failed")


def init_raindrop():
    with open("./Raindrop-token.txt", "r") as f:
        Raindrop_api = API(f.read())
    for collection in Collection.get_collections(Raindrop_api):
        if collection.title == "知乎":
            collection_target = collection
    return Raindrop_api, collection_target


if __name__ == "__main__":
    collection_id = 172817658
    collection_total = get_total(collection_id)
    print("收藏夹总数：{}".format(collection_total))
    Raindrop_api, collection_target = init_raindrop()
    get_singleinfo(Raindrop_api, collection_target, collection_id, collection_total)
