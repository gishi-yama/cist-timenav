import json

import requests
from flask import Flask, jsonify, make_response
from flask_cors import CORS

from timetable_miner import lib

url = 'http://localhost:8081/pdf/bytes'
response = requests.get(url)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/outwards', methods=['GET'])
def outwards():
    out = lib.PdfMiner(response.content).outwards
    return make_response(jsonify(out))


@app.route('/returns')
def returns():
    ret = lib.PdfMiner(response.content).returns
    return make_response(jsonify(ret))


if __name__ == '__main__':
    app.run(port=8080, debug=True)
