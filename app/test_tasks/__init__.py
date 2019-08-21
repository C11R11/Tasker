from flask import Blueprint
test_tasks_blueprint = Blueprint('test_tasks', __name__, template_folder='templates')
from . import sleep_task_views
