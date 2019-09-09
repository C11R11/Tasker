import os, json
from jobs_core.TaskRepo import TaskRepo

ResultsSimpleFilePath = os.path.join('app', 'static', 'results')

class Task:
    #Constructor, define mouse velocity
    def __init__(self, taskId, taskrepo):
        self.taskId = taskId
        self.taskrepo = taskrepo
        self.SourceData = json.loads(self.taskrepo.GetTask(self.taskId))
        self.outPath = os.path.join(os.getcwd(), ResultsSimpleFilePath,  self.taskId , "out")
        if (self.SourceData == ""):
            print ("la tarea no ha sido creada aun")
    
    def IsAFinishedTask(self):
        if self.SourceData["estado"] == "Terminado":
            return True
        return False
    
    def GetAllFilesInput(self):
        path = os.path.join(os.getcwd(), ResultsSimpleFilePath,  self.taskId , "in")
        list_of_files = []
        for filename in os.listdir(path):
            filename = os.path.join("results", self.taskId, "in",filename)
            filename = "/".join(filename.split(os.path.sep))
            list_of_files.append(filename)
        return list_of_files

    def GetAllFilesOutput(self):
        list_of_files = []
        for filename in os.listdir(self.outPath):
            filename = os.path.join("results", self.taskId, "out",filename)
            filename = "/".join(filename.split(os.path.sep))
            list_of_files.append(filename)
        return list_of_files
    
    def GetZipFilename(self):
        self.zipFileName = "files_" + self.taskId + ".zip"
        filename = os.path.join("results", self.taskId, "out",self.zipFileName)
        filename = "/".join(filename.split(os.path.sep))
        return filename
