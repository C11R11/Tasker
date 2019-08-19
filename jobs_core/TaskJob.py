import time, sys, os, json
from jobs_core.TaskRepo import TaskRepo

ResultsSimpleFilePath = os.path.join('app', 'static', 'results')

class TaskJob:
    #Constructor, define mouse velocity
    def __init__(self, taskId, taskrepo):
        self.taskrepo = taskrepo
        self.SourceData = json.loads(self.taskrepo.GetTask(taskId))
    
    def IsAFinishedTask(self):
        if self.SourceData["estado"] == "Terminado":
            return True
        return False
    
    def GetAllFilesInput(self):
        #print("Current Working Directory " , os.getcwd())
        path = os.path.join(os.getcwd(), ResultsSimpleFilePath,  self.SourceData["ID"] , "in")
        #print(path)
        list_of_files = []
        for filename in os.listdir(path):
            filename = os.path.join("results", self.SourceData["ID"], "in",filename)
            filename = "/".join(filename.split(os.path.sep))
            list_of_files.append(filename)
        return list_of_files

    def GetAllFilesOutput(self):
        print("Current Working Directory " , os.getcwd())
        path = os.path.join(os.getcwd(), ResultsSimpleFilePath,  self.SourceData["ID"] , "out")
        print(path)
        list_of_files = []
        for filename in os.listdir(path):
            filename = os.path.join("results", self.SourceData["ID"], "out",filename)
            filename = "/".join(filename.split(os.path.sep))
            list_of_files.append(filename)
        return list_of_files