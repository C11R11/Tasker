import unittest
import time, os
from jobs_core.TaskRepo import TaskRepo
from jobs_core.TaskJob import TaskJob
from jobs_core.TaskCaller import TaskCaller

"""
Cada vez que se escribe un método que parta con "test" se ejecuta nuevamente el SetUp.
Es como un único fixture
"""
class TestTaskJob(unittest.TestCase):
    def setUp(self):
        self.taskRepo = TaskRepo(os.path.join('my_database.sqlite'))
        self.taskjob = TaskJob("test", self.taskRepo)
        self.pathName = os.path.join('app', 'static', 'results', self.taskjob.GetJobId())
        self.exe = "python " + os.path.join(os.getcwd(), 'jobs_core', 'test_exes', 'SleepTaskTest.py ' + str(2))
        self.assertFalse(self.taskjob.TheJobBegan())
        self.assertFalse(self.taskjob.TheJobHasFinished())
    
    def test_DoingJob(self):
        assert self.taskjob.GetJobId() != "", "Should be valid id"
        self.taskjob.StartTask(self.pathName, self.exe)
        self.assertTrue(self.taskjob.TheJobBegan())
        self.assertFalse(self.taskjob.TheJobHasFinished())
        time.sleep(3)
        self.assertTrue(self.taskjob.TheJobBegan())
        self.assertTrue(self.taskjob.TheJobHasFinished())
 
if __name__ == '__main__':
    unittest.main()
    
    
    