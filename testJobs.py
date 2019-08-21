import time, sys, os
from jobs_core.TaskRepo import TaskRepo
from jobs_core.TaskJob import TaskJob

if __name__ == "__main__":
    taskRepo = TaskRepo(os.path.join('my_database.sqlite'))
    taskjob = TaskJob("test", taskRepo)
    pathName = os.path.join('app', 'static', 'results', taskjob.GetJobId())
    exe = "python " + os.path.join(os.getcwd(), 'app', 'executables', 'SleepTaskTest.py ' + str(5))
    taskjob.StartTask(pathName, exe)