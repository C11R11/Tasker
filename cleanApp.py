import os
import shutil
import sqlite3

def cleanApp():
    #Clean results
    pathName = os.path.join(os.getcwd(), 'app', 'static', 'results')
    shutil.rmtree(pathName)
    os.mkdir(pathName)

    #CleanBD
    DELETE_BD = "DELETE from TaskJob"
    conn = sqlite3.connect('my_database.sqlite')
    cursor = conn.cursor()
    cursor.execute(DELETE_BD)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    cleanApp()
