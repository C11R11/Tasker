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
