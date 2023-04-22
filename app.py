from flask import Flask, render_template,request
import chat as c
s = ""
app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'], endpoint='test01')
def hello_world():
    global keys,getData,s
    getData = request.args.to_dict()
    try:
        keys = getData['ky']
        keys+="\n"
        s+="你："+keys
        print(keys)
        s += "机器人："+c.chat(keys)+"\n"
        s = s.replace("抱歉，获取出错！","我也不太会")
        print(s)
    except Exception as e:
        pass
    return render_template('index.html',texts=s)#上传到index.html页面中
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
