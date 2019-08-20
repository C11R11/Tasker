from . import test_tasks_blueprint
from flask import current_app as app
from flask import Flask, render_template, request, redirect, url_for
import json, os, threading
from jobs_core.TaskRepo import TaskRepo
from jobs_core.TaskCaller import TaskCaller
from jobs_core.TaskJob import TaskJob

def TaskThreadSleep(taskId, sleep):
    pathNameOut = os.path.join(os.getcwd(), 'app', 'static', 'results', taskId , "out")
    exe = "python " + os.path.join(os.getcwd(), 'app', 'executables', 'SleepTaskTest.py ' + str(sleep))
    print ("exe->", exe)
    cmd = exe
    task = TaskCaller(cmd, pathNameOut)
    output = task.callTask().stdout
    taskOutput = "<br />".join(output.split("\n"))
    print("output->", output)

    taskrepo = TaskRepo(app.config["BdNameConnection"])
    taskrepo.FinishJob(taskId, taskOutput)

    WriteLog(pathNameOut, output)
    SendEmail(taskId, output)

def WriteLog(pathNameOut, output):
    logFilename = os.path.join(os.getcwd(),  pathNameOut, 'log.txt')
    f = open(logFilename , 'w' )
    f.write(output)
    f.close()

def SendEmail(taskId, output):
    import smtplib

    email = "Tarea id = " + taskId + " Finalizada\n\nDetalle:\n\n__________" + output + "\n\n_________"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(app.config["EmailServerLogin"], app.config["EmailServerLoginPass"])
    server.sendmail(
        app.config["EmailSender"],
    app.config["EmailList"],
    email)
    server.quit()

def MakeNewTaskPaths(taskId):
    pathName = os.path.join(app.config["ResultsSimpleFilePath"], taskId)
    pathNameIn = os.path.join(app.config["ResultsSimpleFilePath"], taskId , "in")
    pathNameOut = os.path.join(app.config["ResultsSimpleFilePath"], taskId , "out")
    os.mkdir(pathName)
    os.mkdir(pathNameIn)
    os.mkdir(pathNameOut)

def StartTaskThread(taskId, segs):
    MakeNewTaskPaths(taskId)
    x = threading.Thread(target=TaskThreadSleep, args=(taskId, segs))
    x.start()

def MakeNewTask():
    taskRepo = TaskRepo(app.config["BdNameConnection"])
    taskname = request.form['nombretarea']
    #print("taskname", taskname)
    taskInfo = json.loads(taskRepo.GetTask(str(taskRepo.CreateTaskJob(taskname))))
    taskId = taskInfo["ID"]
    return taskId

@test_tasks_blueprint.route('/newTaskSleep', methods=['POST'])
def newTaskSleep():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        segs = request.form['segundos']
        StartTaskThread(MakeNewTask(), segs)
    return redirect(url_for("dashboard"))

@test_tasks_blueprint.route('/newtaskForm')
def newtaskForm():
    return render_template('newTaskForm.html')
