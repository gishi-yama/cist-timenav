import json
import os
import re
from enum import Enum
from typing import Tuple, Union

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


class Key(Enum):
    CHITOSE = 'chitose'
    MINAMI_CHITOSE = 'minamiChitose'
    STUDY_BUILDING = 'studyBldg'
    MAIN_BUILDING = 'mainBldg'
    NOTE = 'note'

    @staticmethod
    def times():
        return [Key.CHITOSE.value, Key.MINAMI_CHITOSE.value, Key.STUDY_BUILDING.value, Key.MAIN_BUILDING.value]


class Column:
    TO_SCHOOL = {'千歳駅発': Key.CHITOSE.value, '南千歳駅発': Key.MINAMI_CHITOSE.value,
                 '研究実験棟発': Key.STUDY_BUILDING.value, '本部棟着': Key.MAIN_BUILDING.value, '備考': Key.NOTE.value}
    TO_HOME = {'本部棟発': Key.MAIN_BUILDING.value, '研究実験棟着': Key.STUDY_BUILDING.value,
               '南千歳駅着': Key.MINAMI_CHITOSE.value, '千歳駅着': Key.CHITOSE.value, '備考': Key.NOTE.value}


def initialize() -> Tuple[dict, dict]:
    request_url = url + 'info'
    information = json.loads(requests.get(request_url).content)
    miners = {}
    for ordinal, _ in information.items():
        request_url = url + 'bytes/' + ordinal
        miners[int(ordinal)] = lib.PDFMiner(requests.get(request_url).content)
    return information, miners


titles, pdf_miners = initialize()


@app.route('/info')
def inform():
    return make_response(jsonify({'results': titles}))


@app.route('/table/to/school/<number>')
def to_school_table(number: str):
    to_school_df = pdf_miners[int(number)].to_school_df[Column.TO_SCHOOL.keys()].rename(columns=Column.TO_SCHOOL)
    return make_response(jsonify({'results': to_school_df.to_dict(orient='records')}))


@app.route('/table/to/school/oldest')
def oldest_to_school_table():
    return to_school_table('0')


@app.route('/table/to/school/<number>/timestamp')
def to_school_table_as_ts(number: str):
    to_school_df = pdf_miners[int(number)].to_school_df[Column.TO_SCHOOL.keys()].rename(columns=Column.TO_SCHOOL)
    to_school_df[Key.times()] = to_school_df[Key.times()].applymap(lambda x: str_to_timestamp(x)).replace({pd.NaT: None})
    return make_response(jsonify({'results': to_school_df.to_dict(orient='records')}))


@app.route('/table/to/school/oldest/timestamp')
def oldest_to_school_table_as_ts():
    return to_school_table_as_ts('0')


@app.route('/date/<number>')
def date(number: str):
    date_text = re.search('（.*?）', titles[number]).group(0)
    date_text = date_text.replace('（', '').replace('）', '')
    return make_response(jsonify({'results': date_text}))


@app.route('/date/oldest')
def oldest_date():
    return date('0')


@app.route('/table/to/home/<number>')
def to_home_table(number: str):
    to_home_df = pdf_miners[int(number)].to_home_df[Column.TO_HOME.keys()].rename(columns=Column.TO_HOME)
    return make_response(jsonify({'results': to_home_df.to_dict(orient='records')}))


@app.route('/table/to/home/oldest')
def oldest_to_home_table():
    return to_school_table('0')


@app.route('/table/to/home/<number>/timestamp')
def to_home_table_as_ts(number: str):
    to_home_df = pdf_miners[int(number)].to_home_df[Column.TO_HOME.keys()].rename(columns=Column.TO_HOME)
    to_home_df[Key.times()] = to_home_df[Key.times()].applymap(lambda x: str_to_timestamp(x)).replace({pd.NaT: None})
    return make_response(jsonify({'results': to_home_df.to_dict(orient='records')}))


@app.route('/table/to/home/oldest/timestamp')
def oldest_to_home_table_as_ts():
    return to_home_table_as_ts('0')


def str_to_timestamp(str_formed_time: str) -> Union[None, pd.Timestamp]:
    if str_formed_time is None:
        return str_formed_time
    timestamp = pd.Timestamp(year=1998, month=3, day=24, hour=0, minute=0, second=0)
    time = pd.to_datetime(str_formed_time, format='%H:%M')
    timestamp = timestamp.replace(hour=time.hour, minute=time.minute, second=0, microsecond=0)
    if timestamp is pd.NaT:
        return str_formed_time
    return timestamp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
