from flask import Flask, request
from flask_restplus import Api, Resource, fields
from jobs_api import api
from jobs_core.TaskRepo import TaskRepo
from jobs_core.TaskJob import TaskJob
import os, json

jobs_namespace = api.namespace('api/jobs', description='Manage task jobs')

jobs_model = api.model('New Job',
                    {
                        'nombretarea': fields.String(required=True,
                                                     description="Nombre de la tarea",
                                                     help="requerido."),
                        'segundos': fields.Integer(required=True,
                                                     description="Duración en segundos",
                                                     help="requerido")
                    })


@jobs_namespace.route("/tasks")
class AllJobs(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                     params={ })
    def get(self):
        try:
            taskrepo = TaskRepo('my_database.sqlite')
            allTasks = json.loads(taskrepo.GetTasks())
            return allTasks
        except KeyError as e:
            jobs_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            jobs_namespace.abort(400, e.__doc__, status= "Could not retrieve information", statusCode = "400")

@jobs_namespace.route("/taskInfo/<string:id>")
class TaskInfo(Resource):
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'},
                     params={})
    def get(self, id):
        try:
            taskrepo = TaskRepo('my_database.sqlite')
            print(taskrepo.GetTask(id))
            taskInfo = json.loads(taskrepo.GetTask(id))
            print("getting all jobs")
            return taskInfo
        except KeyError as e:
            jobs_namespace.abort(500, e.__doc__, status="Could not retrieve information", statusCode="500")
        except Exception as e:
            jobs_namespace.abort(400, e.__doc__, status= "Could not retrieve information", statusCode = "400")

@jobs_namespace.route("/newJob")
class NewJob(Resource):
    @api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' })
    @api.expect(jobs_model)        
    def post(self):
        try:
            segs = request.json['segundos']
            taskRepo = TaskRepo('my_database.sqlite')
            print ("58->", request.json['nombretarea'])
            taskjob = TaskJob(request.json['nombretarea'], taskRepo)
            print ("59->", request.json['segundos'])
            pathName = os.path.join(os.getcwd(), 'jobs_api', 'static', 'results', taskjob.GetJobId())
            exe = "python " + os.path.join(os.getcwd(), 'jobs_api', 'static', 'exes', 'SleepTaskTest.py ' + str(segs))
            print ("exe->", exe)
            taskjob.StartTask(pathName, exe)

            return {
                "name": request.json['nombretarea'],
                "status": "New job added",
                "id": taskjob.GetJobId()
            }
        except KeyError as e:
            jobs_namespace.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
        except Exception as e:
            jobs_namespace.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")
