from flask import Flask

from pdf_retriever import lib


pdf_url = lib.HtmlScraper().pdf_url


app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/pdf_url')
def url():
    return pdf_url


@app.route('/pdf/bytes')
def pdf_bytes():
    return lib.Retriever.retrieve(url())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
