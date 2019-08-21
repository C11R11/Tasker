import time, sys, os, json, threading
from jobs_core.TaskRepo import TaskRepo
from jobs_core.TaskCaller import TaskCaller
from jobs_core.utils import *

ResultsSimpleFilePath = os.path.join('app', 'static', 'results')

class TaskJob:
    #Constructor, define mouse velocity
    def __init__(self, taskname, taskrepo):
        self.taskname = taskname
        self.taskrepo = taskrepo
        self.taskId = self.taskrepo.CreateTaskJob(taskname)
        self.SourceData = json.loads(self.taskrepo.GetTask(self.taskId))
        print("self.SourceData-->", self.SourceData)
        if (self.SourceData):
            print ("la tarea no ha sido creada aun")
        self.EmailList = ["cristian.rodriguez@maptek.cl"]
        self.EmailServerLogin = "guitrackbots@gmail.com"
        self.EmailServerLoginPass = "g46ytd72"
        self.EmailSender =  "info@Tasker.cl"

    def GetJobId(self):
        return self.taskId

    def StartTask(self, pathNameBase, exe):
        self.pathNameBase = pathNameBase
        self.pathNameOut = os.path.join(self.pathNameBase, "out")
        self.pathNameIn = os.path.join(self.pathNameBase, "in")
        self.exe = exe
        x = threading.Thread(target=self.ExecuteTask, args=())
        x.start()

    def ExecuteTask(self):
        cmd = self.exe
        self.MakeNewTaskPaths()
        task = TaskCaller(cmd, self.pathNameOut)
        output = task.callTask().stdout
        taskOutput = "<br />".join(output.split("\n"))
        print("output->", output)
        self.taskrepo.FinishJob(self.taskId, taskOutput)

        WriteLog(self.pathNameOut, output)
        SendEmail(self.taskId, 
                    output, 
                    self.EmailServerLogin, 
                    self.EmailServerLoginPass,
                    self.EmailSender,
                    self.EmailList
                    )
    
    def MakeNewTaskPaths(self):
        os.mkdir(self.pathNameBase)
        os.mkdir(self.pathNameIn)
        os.mkdir(self.pathNameOut)

    def IsAFinishedTask(self):
        if self.SourceData["estado"] == "Terminado":
            return True
        return False
    
    def GetAllFilesInput(self):
        #print("Current Working Directory " , os.getcwd())
        path = os.path.join(os.getcwd(), ResultsSimpleFilePath,  self.taskId , "in")
        #print(path)
        list_of_files = []
        for filename in os.listdir(path):
            filename = os.path.join("results", self.taskId, "in",filename)
            filename = "/".join(filename.split(os.path.sep))
            list_of_files.append(filename)
        return list_of_files

    def GetAllFilesOutput(self):
        print("Current Working Directory " , os.getcwd())
        path = os.path.join(os.getcwd(), ResultsSimpleFilePath,  self.taskId , "out")
        print(path)
        list_of_files = []
        for filename in os.listdir(path):
            filename = os.path.join("results", self.taskId, "out",filename)
            filename = "/".join(filename.split(os.path.sep))
            list_of_files.append(filename)
        return list_of_files