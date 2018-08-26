from flask import Flask#,render_template,request,jsonify
from day3spider import getInfos
from pymongo import MongoClient
import json
from bson import json_util
app = Flask(__name__)


client = MongoClient("192.168.1.146",27017)
db = client["morlockdb"]
col = db["zww"]


def GetInfos(user_id, passwd):
    info = col.find({"学号":user_id})
    print(info.count())
    if info.count() == 1:
        #return info.__getitem__(0)
        #return info[0]
        #if info[0]["passwd"] == passwd:
        return json.dumps(info[0],default=json_util.default)
        #else:
        #    return False
    elif info.count() == 0:
        info = getInfos(user_id, passwd)
        #print(info)
        col.insert(info)
        return info

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
        return render_template("info.html",content=content)
@app.route("/apitest")
def apitest():
    return render_template("api.html")


@app.errorhandler(405)
def error(e):
    content = "---405地址写错---"
    return render_template("error.html",content=centent)

@app.errorhandler(404)
def error(e):
    content = "---404地址写错---"
    return render_template("error.html",content=content)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)




