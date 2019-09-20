import time, os
from jobs_core.TaskRepo import TaskRepo
from jobs_core.TaskJob import TaskJob
from jobs_core.TaskCaller import TaskCaller

segs = 5

for x in range(100):
    segs = segs +1
    filename = []
    name = "test name " + str(segs)
    taskRepo = TaskRepo(os.path.join('my_database.sqlite'))
    taskjob = TaskJob(name, taskRepo, filename)
    pathName = os.path.join('app', 'static', 'results', taskjob.GetJobId())
    exe = "python " + os.path.join(os.getcwd(), 'jobs_core', 'test_exes', 'SleepTaskTest.py ' + str(segs))
    taskjob.StartTask(pathName, exe)
    time.sleep(5)