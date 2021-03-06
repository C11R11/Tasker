from . import test_tasks_blueprint
from flask import current_app as app
from flask import Flask, render_template, request, redirect, url_for
import os
from jobs_core.TaskJob import TaskJob
from jobs_core.utils import SendEmail

@test_tasks_blueprint.route('/newTaskSleep', methods=['POST'])
def newTaskSleep():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        segs = request.form['segundos']
        uploaded_files = request.files.getlist("file[]")
        print (uploaded_files)

        taskjob = TaskJob(request.form['nombretarea'], app.config["REPO"], uploaded_files)
        taskjob.SetEmailConfiguration(app.config["EMAIL_SERVER_LOGIN"], 
                                    app.config["EMAIL_SERVER_LOGIN_PASS"],
                                    app.config["EMAIL_SENDER"],
                                    app.config["RESULTS_SIMPLE_FILE_PATH"])
        pathName = os.path.join(os.getcwd(), 'app', 'static', 'results', taskjob.GetJobId())
        exe = "python " + os.path.join(os.getcwd(), 'app', 'executables', 'SleepTaskTest.py ' + str(segs))
        taskjob.StartTask(pathName, exe)
    return redirect(url_for("dashboard"))

@test_tasks_blueprint.route('/newtaskForm')
def newtaskForm():
    return render_template('newTaskForm.html')
