from . import test_tasks_blueprint
from flask import current_app as app
from flask import Flask, render_template, request, redirect, url_for
import os
from jobs_core.TaskRepo import TaskRepo
from jobs_core.TaskJob import TaskJob
from jobs_core.utils import SendEmail

@test_tasks_blueprint.route('/newTaskSleep', methods=['POST'])
def newTaskSleep():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        segs = request.form['segundos']
        taskRepo = TaskRepo(app.config["BdNameConnection"])
        taskjob = TaskJob(request.form['nombretarea'], taskRepo)
        taskjob.SetEmailConfiguration(app.config["EmailServerLogin"], 
                                    app.config["EmailServerLoginPass"],
                                    app.config["EmailSender"],
                                    app.config["EmailList"])
        pathName = os.path.join(os.getcwd(), 'app', 'static', 'results', taskjob.GetJobId())
        exe = "python " + os.path.join(os.getcwd(), 'app', 'executables', 'SleepTaskTest.py ' + str(segs))
        taskjob.StartTask(pathName, exe)
    return redirect(url_for("dashboard"))

@test_tasks_blueprint.route('/newtaskForm')
def newtaskForm():
    return render_template('newTaskForm.html')
