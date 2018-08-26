from flask import Flask, flash, redirect, render_template, request, jsonify
from day3spider import getInfos
from pymongo import MongoClient
from mail import mail
import json
from bson import json_util
app = Flask(__name__)


'''
client = MongoClient("192.168.1.146",27017)
db = client["morlockdb"]
col = db["zww"]
'''
client = MongoClient("192.168.1.146",27017)
db = client.morlockdb
col = db.zww
'''
def GetInfos(user_id, passwd):
    info = col.find({"学号":user_id})
    print(info.count())
    if info.count() == 1:
        #return info.__getitem__(0)
        #return info[0]
        #if info[0]["passwd"] == passwd:
        print('ks1:')
        return json.dumps(info[0],default=json_util.default)
        #else:
        #    return False
    elif info.count() == 0:
        info = getInfos(user_id, passwd)
        print('ks0:')
        col.insert(info)
        return info
'''
        #return json.dumps(info,default=json_until.default)

@app.route("/",methods=["post","GET"])
def index():
    return render_template("index.html")

@app.route("/api",methods=["post","GET"])

def api():
    if request.method == "GET":
        content = "数填错了"
        return render_template("error.html",content=content)
    elif request.method == "POST":
        user_id = request.form["username"]
        password = request.form["password"]
        infos=GetInfos(user_id,password)
        #col.insert(infos)
        #return render_template("info.html",content=content)
        #infos=json.dumps(infos,default=json_util.default)
        res = jsonify(infos)
        res.headers['Access-Control-Allow-Origin'] = '*'.encode("utf-8").decode("latin1")
        res.headers['Access-Control-Allow-Methods'] = 'POST，GET,OPTIONS'.encode("utf-8").decode("latin1")
        res.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'.encode("utf-8").decode("latin1")
        return res

@app.route("/info",methods=["post","GET"])
def showinfo():
    if request.method == "GET":
        content = "数填错了"
        return render_template("error.html",content=content)
    elif request.method == "POST":
        user_id = request.form["username"]
        password = request.form["password"]
        content=getInfos(user_id,password)
        xuehao = json.dumps(content["学号"], ensure_ascii=False)#要想得到字符串的真实表示，需要用到参数ensure_ascii=False(默认为True)：
        xingming = json.dumps(content["姓名"], ensure_ascii=False)
        kms = 0
        #res_cj = json.dumps(content)   #获取全部内容
        #res_cj = json.dumps(content["成绩"])  #获取全部内容中成绩部分
        print(content)
    for idx,cj in enumerate(content["成绩"]):
        idx += 1 
        kms =  idx
        #print(isinstance(content,dict))
        #res_cj = json.dumps(content['成绩'][idx]['课程代码'], ensure_ascii=False)  #获取全部内容中成绩部分 
    print(user_id)
    result = col.find({"user_id":xuehao})  #获取数据库中是否存在
    if result.count() == 0:
        col.insert({"username":xingming,"user_id":xuehao,"password":xuehao,"kms":kms})  #如果不存在则添加
    else:
       for c in result:
          get_kms = c.get("kms")
          print(xuehao)
          col.update({"username":xingming},{'$set':{"kms":get_kms}})  #否则更新
          if get_kms != kms:
            #print('http://192.168.1.146/score?username='+eval(xuehao)+'&password='+eval(xuehao)+'')
            mail("2364173153@qq.com","http://192.168.1.146/score?username="+eval(xuehao)+"&password="+eval(xuehao))
    return render_template("info.html",content = content)
'''    
    for idx,grades in enumerate(res_cj):
        get_cj = int(grades["总评成绩"])
        #get_cj[idx] = json.dumps(grades["总评成绩"], ensure_ascii=False)
        print(get_cj)
    
        #print('xm:'+ xingming)
        #print(xuehao)
        result = db.zww.find_one({"user_id":user_id})  #获取数据库中是否存在
        #print(result)
    if result is None:
       db.zww.insert({"username":xingming,"user_id":xuehao,"password":xuehao})  #如果不存在则添加
       #res_cj = json.dumps(content)
       res_cj = json.dumps(content["成绩"], ensure_ascii=False)
       #print(res_cj)
       
       for idx,grades in enumerate(res_cj):
        #get_cj = grades["成绩"]["总评成绩"]
        get_cj[idx] = json.dumps(grades["总评成绩"], ensure_ascii=False)
        print(get_cj[idx])
'''
@app.route('/score',methods=["post","GET"])
def score():
    user_id = request.args.get('username', '')
    password = request.args.get('password', '')
    #print(user_id)
    content=getInfos(user_id,password)
    #print(content)
    return render_template("score.html",content = content)
    #return render_template('/score.html')

#@app.route("/score?username=<username>&password=<password>")
#def score(username,password):
    #print(username)
'''
   

def content(a,b,c):
    print(a,b)
    a=func.__code__.co_argcount
    print(a)
 

'''

@app.route("/apitest")
def apitest():
    return render_template("api.html")


@app.errorhandler(405)
def error(e):
    content = "---405地址写错---"
    return render_template("error.html",content=content)

@app.errorhandler(404)
def error(e):
    print(e)
    content = "---404地址写错---"
    return render_template("error.html",content=content)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)

