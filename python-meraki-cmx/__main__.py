from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
	return jsonify({'text':'Hello World!'})

class Events(Resource):
	def post(self):
		print (self);
		return '8edf4ae18d782e5ac90512bc7db3850038879397'

	def get(self):
		return jsonify({'text':'Hello World!'})

class Events_Info(Resource):
	def post(self, events_info):
		print(self)
		print(events_info)


api.add_resource(Events, '/events')
api.add_resource(Events_Info, '/events/<events_info>')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5002)