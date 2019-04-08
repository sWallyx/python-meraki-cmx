#!/usr/bin/env python
# coding=utf-8
from pprint import pprint
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import json
from flask_jsonpify import jsonify
import sys, getopt
import pymongo
import ast

app = Flask(__name__)
api = Api(app)

validator = '8edf4ae18d782e5ac90512bc7db3850038879397'
secret = 'nosfnoqf3276293r'
version = '2.0'
CORS(app)

def save_data(data):
    print("---- SAVING CMX DATA ----")
    # CHANGE ME - send 'data' to a database or storage system
    #pprint(data, indent=1)
    parsed = json.dumps(data)
    #print parsed
    connection = pymongo.MongoClient('mongodb://localhost')
    col = connection.locations.events
    col.insert(json.loads(parsed))
    #parsed = json.loads(data)

    #for item in parsed:
        #record1.insert(item)
        #print item

@app.route('/', methods=['GET'])
def get_validator():
    print("validator sent to: ",request.environ['REMOTE_ADDR'])
    return validator

# Accept CMX JSON POST
@app.route('/', methods=['POST'])
def get_cmxJSON():
    if not request.json or not 'data' in request.json:
        return("invalid data",400)
    cmxdata = request.json
    #pprint(cmxdata, indent=1)
    print("Received POST from ",request.environ['REMOTE_ADDR'])

    # Verify secret
    if cmxdata['secret'] != secret:
        print("secret invalid:", cmxdata['secret'])
        return("invalid secret",403)
    else:
        print("secret verified: ", cmxdata['secret'])

    # Verify version
    if cmxdata['version'] != version:
        print("invalid version")
        return("invalid version",400)
    else:
        print("version verified: ", cmxdata['version'])

    # Determine device type
    if cmxdata['type'] == "DevicesSeen":
        print("WiFi Devices Seen")
    elif cmxdata['type'] == "BluetoothDevicesSeen":
        print("Bluetooth Devices Seen")
    else:
        print("Unknown Device 'type'")
        return("invalid device type",403)

    # Do something with data (commit to database)
    save_data(cmxdata)

    # Return success message
    return "CMX POST Received"

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5002)
