import artitle as at
import random as rd
import json
import requests as r
from loguru import logger as log

wh = ['hello','你好','好久不见','见到你真开心']
hd = ['你好呀','嗯嗯']
def chat(key):
    key=key.strip("帮我一下可以吗谢谢，。")
    for i in wh:
        if i in key:
            log.debug("start randint")
            s = rd.randint(1,2)
            
            if s == 1:
                log.debug("s = 1")
                log.debug("output "+hd[0])
                return hd[0]
            elif s == 2:
                log.debug("s = 2")
                log.debug("output "+hd[1])
                return hd[1]
    if "文章" in key:
        key=key.strip("帮我一下关于篇可以吗谢谢写，。")
        log.debug(key)
        return at.文章(key)
    if "查询" or "差" in key:
        if "电影" in key:
            key=key.strip("查询电影名帮我一下可以吗谢谢，。")
            log.debug(key)
            rs = r.get('https://xiaoapi.cn/API/dy_tx.php?msg='+key+'&n=1&num=8')
            rt = rs.json()
            if rt['code'] == "201":
                return "找不到这个电影"
            else:
                rs1 = "电影名："+rt['title']+"\n人物："+rt['actors']+"\n播放链接："+rt['url']
                return rs1
        if "网址" or "网站" or "url" or "URL" in key:
            key=key.strip("查询网址网站urlURL帮我一下可以吗谢谢，。:：")
            log.debug(key)
            rs = r.get('https://xiaoapi.cn/API/zs_wzxx.php?url='+key)
            rt = rs.json()
            if rt['code'] == "201":
                return "找不到这个网站"
            else:
                try:
                    rs1 = "标题："+rt['title']+"\nkeyword:"+rt['keyword']+"\ndescription:"+rt['description']+"\n图标:"+rt['icon']+"\n备案:"+rt['icp']
                    return rs1
                except:
                    try:
                        key=key.strip("查询网址网站urlURL帮我一下可以吗谢谢，。:：")
                        key=key.strip("查询电影名帮我一下可以吗谢谢，。")
                        log.debug(key)
                        s = r.get("https://xiaoapi.cn/API/bk.php?m=json&type=bd&msg="+key)
                        a = s.json()
                        return a['msg']
                    except:
                        return "查找失败"
    else:
        return "cnchat听不懂..."
    
if __name__ == "__main__":
    while(1):
        a = input(">>")
        print(chat(a))
