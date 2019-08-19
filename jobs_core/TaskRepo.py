import sqlite3, os, json
import hashlib
import time

class TaskRepo:

    #Path to be indepent from context
    internalPath = os.path.abspath(os.path.dirname(__file__))

    #Constructor, define mouse velocity
    def __init__(self, BdNameConnection):
        self.QUERY_ELAPSED_MINUTES = "strftime('%M minutos', julianday('now') - julianday(creation)) as elapsed "
        self.QUERY_ENDTIME_MINUTES = "strftime('%M minutos', julianday(ended) - julianday(creation)) as endtime "
        self.QUERY_COLUMNS_BASE = "ID, creation, ended, user, ejecutable, estado, output, name"
        self.QUERY_SELECT_ALL_TASKS = "SELECT " + self.QUERY_COLUMNS_BASE + ", " + self.QUERY_ELAPSED_MINUTES + ", " +self.QUERY_ENDTIME_MINUTES + "FROM TaskJob"
        self.QUERY_SELECT_SINGLE_TASK = self.QUERY_SELECT_ALL_TASKS + " where id=?"
        self.QUERY_INSERT_SINGLE_TASK = "INSERT INTO TaskJob VALUES(?, strftime('%Y-%m-%d %H:%M:%S' ,'now'), '', 'usuario1', 'update with points', 'Ejecutandose', '', ?)"
        self.QUERY_UPDATE_FINISH_JOB = "UPDATE TaskJob SET estado = 'Terminado', output = ?, ended = strftime('%Y-%m-%d %H:%M:%S' ,'now') where id=?"
        self.BdNameConnection = BdNameConnection

    def CreateTaskJob(self, name = "default name"):
        self.idTaskJob = self.GetUniqueHash()
        con = sqlite3.connect(self.BdNameConnection)
        cur = con.cursor()
        cur.execute(self.QUERY_INSERT_SINGLE_TASK, (self.idTaskJob, name))
        con.commit()
        con.close()
        return self.idTaskJob

    def GetUniqueHash(self):
        hash = hashlib.sha1()
        hash.update(str(time.time()).encode('utf-8'))
        return hash.hexdigest()[:10]
        
    def GetTask(self, id):
        con = sqlite3.connect(self.BdNameConnection)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute(self.QUERY_SELECT_SINGLE_TASK, (id,))
        con.commit()
        result = cur.fetchone()
        con.close()
        return json.dumps(result)
    
    def FinishJob(self, Id, status):
        conn = sqlite3.connect(self.BdNameConnection)
        cursor = conn.cursor()
        cursor.execute(self.QUERY_UPDATE_FINISH_JOB, (status, Id))
        conn.commit()
        conn.close()

    def GetTasks(self):
        con = sqlite3.connect(self.BdNameConnection)
        con.row_factory = self.dict_factory
        cur = con.cursor()
        cur.execute(self.QUERY_SELECT_ALL_TASKS)
        con.commit()
        result = cur.fetchall()
        con.close()
        return json.dumps(result)

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d        