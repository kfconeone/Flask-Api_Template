import json

from flask import Flask
from flask import request

from .. import app
from ..models.sample_models import *

#這裡是基本route
@app.route("/")
def hello():
    return 'This is default response'


#這裡是自訂URL的方法
@app.route("/<parameter1>")
def hello2(parameter1=None):
    mStatus = Player_Status.query.filter_by(AccountName='GM0000000002').first()
    print(mStatus.NickName)
    return json.dumps(mStatus)


#這裡是Post的方法
@app.route("/post", methods=['GET', 'POST'])
def post_somthing():
    if request.method == 'POST':
        data = request.get_json()
        print(data)

    return json.dumps(data)

####以下是SQL CRUD 基本操作####

#Create


