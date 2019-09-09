from flask import Flask
import os

app = Flask(__name__)

from .test_tasks import test_tasks_blueprint
app.register_blueprint(test_tasks_blueprint, url_prefix='/test_tasks')

from app import admin_views
from app import tasks_views
from jobs_core.TaskRepo import TaskRepo

app.config["EmailList"] = ["cristian.rodriguez@maptek.cl"]
app.config["EmailServerLogin"] = "guitrackbots@gmail.com"
app.config["EmailServerLoginPass"] = "g46ytd72"
app.config["EmailSender"] =  "info@Tasker.cl"
app.config["ResultsSimpleFilePath"] = os.path.join('app', 'static', 'results')
app.config["BdNameConnection"] = os.path.join(os.getcwd(), 'my_database.sqlite')
app.config["TaskRepo"] = TaskRepo(app.config["BdNameConnection"])
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
