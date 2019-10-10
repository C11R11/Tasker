import os
import shutil
import sqlite3

def cleanApp():
    #Clean results
    pathName = os.path.join(os.getcwd(), 'app', 'static', 'results')

    BDDevFile = os.path.join(os.getcwd(), 'app', 'dev_tasker.sqlite')
    if os.path.isfile(BDDevFile):
        print("Eliminando ", BDDevFile)
        os.remove(BDDevFile)
    BDTestFile = os.path.join(os.getcwd(), 'app', 'test_tasker.sqlite')
    if os.path.isfile(BDTestFile): 
        print("Eliminando ", BDTestFile)
        os.remove(BDTestFile)
    
    if os.path.exists(pathName):
        print("Eliminando resultados")
        shutil.rmtree(pathName)
    os.mkdir(pathName)

if __name__ == "__main__":
    cleanApp()
