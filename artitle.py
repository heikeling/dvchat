import random,dataread

data = dataread.read_json(r"data.json")
famous = data["famous"] # a 代表前面垫话，b代表后面垫话
before = data["before"] # 在名人名言前面弄点废话
content_list = []
after = data['after']  # 在名人名言后面弄点废话
bosh = data['bosh'] # 代表文章主要废话来源

xx = "学生会退会"

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for i in 池:
            yield i

下一句废话 = 洗牌遍历(bosh)
下一句名人名言 = 洗牌遍历(famous)

def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(before) )
    xx = xx.replace(  "b",random.choice(after) )
    return xx

def 另起一段():
    xx = "。"
    xx += "\r\n"
    xx += "    "
    return xx

def 文章(xx):
    for x in xx:
        tmp = str()
        while ( len(tmp) < 3000 ) :
            分支 = random.randint(0,100)
            if 分支 < 5:
                tmp += 另起一段()
            elif 分支 < 20 :
                tmp += 来点名人名言()
            else:
                tmp += next(下一句废话)
        tmp = tmp.replace("x",xx)
        return tmp

