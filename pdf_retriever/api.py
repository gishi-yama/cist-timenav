from flask import Flask, make_response, jsonify

from pdf_retriever import lib

app = Flask(__name__)
retriever = lib.Retriever()


@app.route('/url/oldest')
def oldest_url():
    return make_response(jsonify({'url': retriever.retrieve_url(0)}))


@app.route('/bytes/oldest')
def oldest_bytes():
    return app.response_class(retriever.retrieve_bytes(0), mimetype='text/pdf')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
