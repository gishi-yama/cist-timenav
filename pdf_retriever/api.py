from flask import Flask, make_response, jsonify

from pdf_retriever import lib

app = Flask(__name__)
retriever = lib.Retriever()


@app.route('/info')
def inform():
    return make_response(jsonify(retriever.inform()))


@app.route('/url/oldest')
def oldest_url():
    return make_response(jsonify({'url': retriever.retrieve_url(0)}))


@app.route('/url/<number>')
def url_by(number: int):
    return make_response(jsonify({'url': retriever.retrieve_url(number)}))


@app.route('/bytes/oldest')
def oldest_bytes():
    return app.response_class(retriever.retrieve_bytes(0), mimetype='text/pdf')


@app.route('/bytes/<number>')
def bytes_by(number: int):
    return app.response_class(retriever.retrieve_bytes(number), mimetype='text/pdf')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
