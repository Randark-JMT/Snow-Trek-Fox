# Snow Trek Fox - 雪地行狐

> 何为雪地行狐？
>
> 据说，狐狸在雪地上行动时，会用尾巴在雪地上左右甩动，借此抹除掉自己在雪地上面的痕迹
>
> 对每个人来说，总有各种理由需要抹掉自己曾经的痕迹，可能是当年的年少轻狂，可能是自己的黑历史等等，这个脚本将提供一个给每个人在互联网这个大雪地上抹除自己痕迹的机会
>
> （服务器总会有历史的，这个脚本能做的，只是在公开界面上进行抹除痕迹而已）
>
> 使用前仍请默念三遍：互联网是有记忆的

一个 demo ，目的是将互联网收藏夹/足迹进行提取，并将数据保存于 Raindrop 或导出为离线文件

> 运行脚本需要Python 3.10以上版本

目前开发目标：

- Bilibili
  - Bilibili 收藏夹 `GET https://api.bilibili.com/x/v3/fav/folder/created/list?pn=1&ps=10&up_mid=<>`
  - Bilibili 动态 `GET https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space?host_mid=<>`
  - Bilibili 点赞过的视频 `GET https://api.bilibili.com/x/space/like/video?vmid=<>`
  - Bilibili 追番 `GET https://api.bilibili.com/x/space/bangumi/follow/list?vmid=<>&type=1`
  - Bilibili 关注
- 知乎
  - 知乎 收藏夹
  - 知乎 回答
  - 知乎 点赞
  - 知乎 关注
- 微博
  - 微博 点赞
  - 微博 收藏夹
  - 微博 关注

## 为什么是 Raindrop

因为作者平时习惯使用 Raindrop ，如果有其他推荐的平台，欢迎提 issue

## 参考

[atsuoishimoto / python-raindropio](https://github.com/atsuoishimoto/python-raindropio#usage)
