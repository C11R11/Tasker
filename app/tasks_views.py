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
