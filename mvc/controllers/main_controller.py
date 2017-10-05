import json
from .. import app
from .. import db
from ..models.main_models import User

from flask import Flask
from flask import request

@app.route("/")
def hello():
    users = User.query.all()
    print(users)
    print(type(users))
    tuples = [(user.Name,user.age) for user in users]
    return json.dumps(dict(tuples))

@app.route("/post", methods=['GET', 'POST'])
def post_somthing():
    if request.method == 'POST':
        data = request.get_json()
        print(data)

    return json.dumps(data)



