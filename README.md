# Spider for Wechat Official Accounts

## mp.wexin.qq.com
Based on the reprint feature of logined wechat official accounts.

Refer to [CSDN 爬取微信公众号发布的所有文章（包括阅读数，在看数，点赞数）](https://blog.csdn.net/qq_45722494/article/details/120191233)

1. get url (inspect and fill in `cookie`)
create mp.wexin.qq.com/.env
```ini
COOKIE = your cookie
```
2. get html page
3. parse html

## sogou_wechat
- 使用搜狗提供的微信搜索。
- 需要填写cookie
    - 创建 sogou_wechat/.env，并填入
```ini
COOKIE = 你的cookie
```

## bing
- 使用 Bing 提供搜索(偏题了)。
- 需要填写cookie
- 创建 bing/.env并填入
```ini
COOKIE = 你的cookie
```