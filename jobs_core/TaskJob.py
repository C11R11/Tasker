import time, sys, os, json, threading
from jobs_core.TaskRepo import TaskRepo
from jobs_core.TaskCaller import TaskCaller
from jobs_core.utils import *
import shutil
from werkzeug.utils import secure_filename

class TaskJob:
    def __init__(self, taskname, taskrepo, uploaded_files):
        self.taskname = taskname
        self.taskrepo = taskrepo
        self.taskId = self.taskrepo.CreateTaskJob(taskname)
        self.JobInitialized = False
        self.JobFinished = False
        self.PrintJobStatus()
        self.IsEmailConfigured = False
        self.UploadedFiles = uploaded_files
        self.filesPaths = []

    def GetJobId(self):
        return self.taskId

    def TheJobBegan(self):
        return self.JobInitialized

    def TheJobHasFinished(self):
        return self.JobFinished
    
    def PrintJobStatus(self):
        print("self.JobInitialized->", self.JobInitialized)
        print("self.JobFinished->", self.JobFinished)

    def StartTask(self, pathNameBase, exe):
        self.pathNameBase = pathNameBase
        self.pathNameOut = os.path.join(self.pathNameBase, "out")
        self.pathNameIn = os.path.join(self.pathNameBase, "in")
        self.exe = exe
        self.JobInitialized = True

        self.MakeNewTaskPaths()

        for file in self.UploadedFiles:
            filename = secure_filename(file.filename)
            file.save(os.path.join(self.pathNameOut, filename))
            self.filesPaths.append(os.path.join(self.pathNameOut, filename))

        x = threading.Thread(target=self.ExecuteTask, args=())
        x.start()

    def ExecuteTask(self):
        cmd = self.exe
        task = TaskCaller(cmd, self.pathNameOut)
        output = task.callTask().stdout
        taskOutput = "<br />".join(output.split("\n"))
        self.taskrepo.FinishJob(self.taskId, taskOutput)
        self.JobFinished = True

        self.CopyOutFilesToIn()

        WriteLog(self.pathNameOut, output)
        if (self.IsEmailConfigured):
            SendEmail(self.taskId, 
                    output, 
                    self.EmailServerLogin, 
                    self.EmailServerLoginPass,
                    self.EmailSender,
                    self.EmailList
                    )
    
    def CopyOutFilesToIn(self):
        for pathname in self.filesPaths:
            shutil.move(pathname, self.pathNameIn)
   
    def SetEmailConfiguration(self, EmailList, EmailServerLogin, EmailServerLoginPass, EmailSender):
        self.EmailList = EmailList
        self.EmailServerLogin = EmailServerLogin
        self.EmailServerLoginPass = EmailServerLoginPass
        self.EmailSender = EmailSender
        self.IsEmailConfigured = False

    def MakeNewTaskPaths(self):
        os.mkdir(self.pathNameBase)
        os.mkdir(self.pathNameIn)
        os.mkdir(self.pathNameOut)
