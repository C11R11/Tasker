from flask import Flask
import os

app = Flask(__name__)

from app import views
from app import TaskRepo
from app import TaskCaller
from app import TaskJob

app.config["EmailList"] = [""]
app.config["EmailServerLogin"] = ""
app.config["EmailServerLoginPass"] = ""
app.config["EmailSender"] =  ""
app.config["ResultsSimpleFilePath"] = os.path.join('app', 'static', 'results')
app.config["BdNameConnection"] = 'my_database.sqlite'
