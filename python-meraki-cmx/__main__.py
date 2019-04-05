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

	def get(self):
		return jsonify({'text':'Hello World!'})

class Events_Info(Resource):
	def post(self, events_info):
		print(self)
		print(events_info)


api.add_resource(Events, '/events')
api.add_resource(Events_Info, '/events/<events_info>')

if __name__ == '__main__':
	app.run(port=5002)