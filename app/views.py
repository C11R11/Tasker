from app import app
from app.TaskRepo import TaskRepo
from app.TaskJob import TaskJob
from app.TaskCaller import TaskCaller

import os
import sys
import json
import threading
import time

from flask import Flask, render_template, request, redirect, url_for

@app.route("/")
def landing():
    return redirect(url_for("dashboard"))

@app.route("/login")
def main():
    return render_template('login.html')

@app.route("/catalogue")
def catalogue():
    return render_template('catalogue.html')


@app.route("/plans")
def plans():
    return render_template('plans.html')

@app.route("/dashboard")
def dashboard():
    taskrepo = TaskRepo()
    allTasks = json.loads(taskrepo.GetTasks())
    tasks_render = []
    if allTasks == []:
        return render_template('emptyList.html')
    else:
        for taskInfo in allTasks:
            taskJob = TaskJob(taskInfo["ID"])
            badge = "warning"
            if taskJob.IsAFinishedTask():
                badge = "success"
            tasks_render.append(render_template(
                'taskWidgetFlat.html', task=taskInfo, badge=badge, taskJob=taskJob))
        return render_template('dashboard.html', tasks=tasks_render)


def StatusOfTheTask(taskInfo, taskJob):
    return render_template('newTaskWorking.html',  task=taskInfo, widget=GetWidgetForTask(taskInfo["ID"]), taskJob=taskJob)

def GetWidgetForTask(id):
    render_template('taskWidget.html', taskId=id)
    return ""

@app.route("/taskStatus/<tasknewID>")
def taskStatus(tasknewID):
    taskrepo = TaskRepo()
    taskInfo = json.loads(taskrepo.GetTask(tasknewID))
    taskJob = TaskJob(tasknewID)
    return StatusOfTheTask(taskInfo, taskJob)

def TaskThreadSleep(taskId, sleep):
    pathNameOut = os.path.join(os.getcwd(), 'app', 'static', 'results', taskId , "out")
    exe = "python " + os.path.join(os.getcwd(), 'app', 'executables', 'SleepTaskTest.py ' + str(sleep))
    print ("exe->", exe)
    cmd = exe
    task = TaskCaller(cmd, pathNameOut)
    output = task.callTask().stdout
    taskOutput = "<br />".join(output.split("\n"))
    print("output->", output)

    taskrepo = TaskRepo()
    taskrepo.FinishJob(taskId, taskOutput)

    logFilename = os.path.join(os.getcwd(),  pathNameOut, 'log.txt')
    f = open(logFilename , 'w' )
    f.write(output)
    f.close()

    import smtplib

    email = "Tarea id = " + taskId + " Finalizada\n\nDetalle:\n\n__________" + output + "\n\n_________"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(app.config["EmailServerLogin"], app.config["EmailServerLoginPass"])
    server.sendmail(
        app.config["EmailSender"],
    app.config["EmailList"],
    email)
    server.quit()

@app.route('/newTaskSleep', methods=['POST'])
def newTaskSleep():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        segs = request.form['segundos']
        task = TaskRepo()
        taskname = request.form['nombretarea']
        #print("taskname", taskname)
        taskInfo = json.loads(task.GetTask(str(task.CreateTaskJob(taskname))))
        taskId = taskInfo["ID"]
        pathName = os.path.join(app.config["ResultsSimpleFilePath"], taskId)
        pathNameIn = os.path.join(app.config["ResultsSimpleFilePath"], taskId , "in")
        pathNameOut = os.path.join(app.config["ResultsSimpleFilePath"], taskId , "out")
        os.mkdir(pathName)
        os.mkdir(pathNameIn)
        os.mkdir(pathNameOut)
        x = threading.Thread(target=TaskThreadSleep, args=(taskId, segs))
        x.start()
    return redirect(url_for("dashboard"))

@app.route('/newtaskForm')
def newtaskForm():
    return render_template('newTaskForm.html')
