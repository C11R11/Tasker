import time, sys, os, subprocess

class TaskCaller:
    #Constructor, define mouse velocity
    def __init__(self, cmd, cwd = os.getcwd() ):
        self.cmd = cmd
        self.cwd = cwd

    def callTask(self):
        result = subprocess.run(self.cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True, cwd = self.cwd)
        return result

if __name__ == "__main__":
    sleep = 5
    exe = 'python SleepTaskTest.py ' + str(sleep)
    print("exe->", exe)
    cmd = exe
    print("cmd->", cmd)
    task = TaskCaller(cmd, os.path.join(os.getcwd(), "executables"))
    output = task.callTask().stdout
