from flask import Flask, request
from flask_restplus import Api, Resource, fields
from jobs_api import api

test_namespace = api.namespace('api/names', description='Manage names')

model = api.model('Name Model', 
				  {'name': fields.String(required = True, 
    					  				 description="Name of the person", 
    					  				 help="Name cannot be blank.")})

list_of_names = {}

@test_namespace.route("/<string:id>")
class Detail(Resource):

	@api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the person' })
	def get(self, id):
		try:
			name = list_of_names[id]
			return {
				"status": "Person retrieved",
				"name" : list_of_names[id]
			}
		except KeyError as e:
			test_namespace.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
		except Exception as e:
			test_namespace.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

	@api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the person' })
	@api.expect(model)		
	def post(self, id):
		try:
			list_of_names[id] = request.json['name']
			return {
				"status": "New person added",
				"name": list_of_names[id]
			}
		except KeyError as e:
			test_namespace.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			test_namespace.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")


@test_namespace.route("/")
class FullList(Resource):

	@api.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={  })
	def get(self):
		try:
			jsonList = []
			for name in list_of_names:
				jsonList.append({
				"status": "Person retrieved",
				"name" : name})
			return jsonList
		except KeyError as e:
			test_namespace.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
		except Exception as e:
			test_namespace.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")