from app import app
from flask import Flask, render_template, request, redirect, url_for
import json
from jobs_core.Task import Task

@app.route("/dashboard")
def dashboard():
    allTasks = json.loads(app.config["TaskRepo"].GetTasks())
    tasks_render = []
    if allTasks == []:
        return render_template('emptyList.html')
    else:
        for taskInfo in allTasks:
            taskJob = Task(taskInfo["ID"], app.config["TaskRepo"])
            badge = "warning"
            if taskJob.IsAFinishedTask():
                badge = "success"
            tasks_render.append(render_template(
                'taskWidgetFlat.html', task=taskInfo, badge=badge, taskJob=taskJob))
        return render_template('dashboard.html', tasks=tasks_render)

def StatusOfTheTask(taskInfo, taskJob):
    return render_template('TaskInfo.html',  task=taskInfo, widget=GetWidgetForTask(taskInfo["ID"]), taskJob=taskJob)

def GetWidgetForTask(id):
    render_template('taskWidget.html', taskId=id)
    return ""

@app.route("/taskStatus/<tasknewID>")
def taskStatus(tasknewID):
    taskInfo = json.loads(app.config["TaskRepo"].GetTask(tasknewID))
    taskJob = Task(tasknewID, app.config["TaskRepo"])
    return StatusOfTheTask(taskInfo, taskJob)

@app.route("/catalogue")
def catalogue():
    return render_template('catalogue.html')