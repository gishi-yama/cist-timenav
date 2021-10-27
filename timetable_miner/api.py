import os

import numpy as np
import pandas as pd
import requests
from flask import Flask, jsonify, make_response

from timetable_miner import lib

try:
    retriever = os.environ['RETRIEVER']
    url = 'http://{}/'.format(retriever)
except KeyError:
    url = 'http://localhost:8082/'

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def translate_key_to_eng(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={
        '千歳駅発': 'chitose', '南千歳駅発': 'minamiChitose', '研究実験棟発': 'studyBldg', '本部棟着': 'mainBldg',
        '本部棟発': 'mainBldg', '研究実験棟着': 'studyBldg', '南千歳駅着': 'minamiChitose', '千歳駅着': 'chitose',
        '備考': 'note'})
    return df


def str_to_timestamp(str_formed_time: str, year: int = None, month: int = None, day: int = None) -> pd.Timestamp:
    if str_formed_time == '-':
        return str_formed_time
    timestamp = pd.Timestamp.now()
    if year is not None and month is not None and day is not None:
        timestamp = pd.Timestamp(year=year, month=month, day=day)
    time = pd.to_datetime(str_formed_time, format='%H:%M')
    timestamp = timestamp.replace(hour=time.hour, minute=time.minute, second=0, microsecond=0)
    return timestamp


@app.route('/to/school/oldest')
def oldest_to_school():
    request_url = url + 'bytes/oldest'
    buffers = [requests.get(request_url).content]
    df = lib.PDFMiner(buffers).read(0).replace({'―': '-', np.NAN: '-'}).mine_to_school()
    df['備考'] = df['備考'].apply(lambda x: str(x).replace('\r', '\n'))
    df = translate_key_to_eng(df)
    return make_response(jsonify({'results': df.to_dict(orient='records')}))


@app.route('/to/school/oldest/timestamp')
def oldest_to_school_with_timestamp():
    request_url = url + 'bytes/oldest'
    buffers = [requests.get(request_url).content]
    df = lib.PDFMiner(buffers).read(0).replace({'―': '-', np.NAN: '-'}).mine_to_school()
    df['備考'] = df['備考'].apply(lambda x: str(x).replace('\r', '\n'))
    df[['千歳駅発', '南千歳駅発', '研究実験棟発', '本部棟着']] = df[['千歳駅発', '南千歳駅発', '研究実験棟発', '本部棟着']].applymap(lambda x: str_to_timestamp(x))
    df = translate_key_to_eng(df)
    return make_response(jsonify({'results': df.to_dict(orient='records')}))


@app.route('/to/chitose/oldest')
def oldest_to_chitose():
    request_url = url + 'bytes/oldest'
    buffers = [requests.get(request_url).content]
    df = lib.PDFMiner(buffers).read(0).replace({'―': '-', np.NAN: '-'}).mine_to_chitose()
    df['備考'] = df['備考'].apply(lambda x: str(x).replace('\r', '\n'))
    df = translate_key_to_eng(df)
    return make_response(jsonify({'results': df.to_dict(orient='records')}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
