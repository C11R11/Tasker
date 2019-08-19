from flask import Flask
import os

app = Flask(__name__)

from app import admin_views
from app import sleep_task_views
from app import tasks_views

app.config["EmailList"] = [""]
app.config["EmailServerLogin"] = ""
app.config["EmailServerLoginPass"] = ""
app.config["EmailSender"] =  ""
app.config["ResultsSimpleFilePath"] = os.path.join('app', 'static', 'results')
app.config["BdNameConnection"] = 'my_database.sqlite'
