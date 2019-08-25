from flask import Flask, request
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
api = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Name Recorder", 
		  description = "Manage names of various users of the application")

from jobs_api import test_namespace
from jobs_api import jobs_namespace