from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object("app.config.TestingConfig")
print(app.config)

print(app.config)
db = SQLAlchemy(app)
from app.models import TaskJob
db.create_all()

from jobs_core.TaskRepo import TaskRepo
app.config["REPO"] = TaskRepo(app.config["DB_NAME_CONNECTION"])

#Views and others

from app import admin_views
from app import tasks_views

from .test_tasks import test_tasks_blueprint
app.register_blueprint(test_tasks_blueprint, url_prefix='/test_tasks')
