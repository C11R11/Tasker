# coding: utf-8
'''from flask import Flask, request
from flask import render_template
from flask import redirect'''
from flask_sqlalchemy import SQLAlchemy
import hashlib
import datetime
import time
import json
from collections import OrderedDict
from app import db

'''app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)'''

class TaskJob(db.Model):
    __tablename__ = 'TaskJob'
    ID = db.Column(db.Text, primary_key=True)
    creation = db.Column(db.Text, nullable=False, default=datetime.datetime.utcnow)
    ended = db.Column(db.Text, server_default=db.text("''"))
    user = db.Column(db.Text, nullable=False, default="")
    ejecutable = db.Column(db.Text, nullable=False, default="")
    estado = db.Column(db.Integer, nullable=False, server_default=db.text("'En ejecución'"))
    output = db.Column(db.Text, server_default=db.text("'En ejecución'"))
    name = db.Column(db.Text, nullable=False)

    def __init__(self, name):
        self.ID = self.GetUniqueHash()
        self.name = name
    
    def __repr__(self):
        return self.ToJson()

    def GetUniqueHash(self):
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()[:10]

    def ToJson(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return json.dumps(result)

if __name__ == '__main__':
    task = TaskJob("nombre")
    db.session.add(task)
    db.session.commit()

    tasks = TaskJob.query.all()
    for task in tasks:
        print(task.__repr__())
    
    atask = task.GetTask("a6f0c699e8")
    print("nuevo--->")
    print(atask.__repr__())

