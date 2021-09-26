import json

import requests
from flask import Flask

from timetable_miner import lib

url = 'http://localhost:8081/pdf/bytes'
response = requests.get(url)


app = Flask(__name__)


@app.route('/')
def outwards_and_returns():
    return json.dumps(lib.PdfMiner(response.content).outwards_and_returns(),
                      ensure_ascii=False)


@app.route('/outwards')
def outwards():
    return json.dumps(lib.PdfMiner(response.content).outwards,
                      ensure_ascii=False)


@app.route('/returns')
def returns():
    return json.dumps(lib.PdfMiner(response.content).outwards,
                      ensure_ascii=False)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
