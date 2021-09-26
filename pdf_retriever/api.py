from flask import Flask

from pdf_retriever import lib


app = Flask(__name__)


@app.route('/pdf_url')
def url():
    return lib.HtmlScraper().pdf_url


@app.route('/pdf/bytes')
def pdf_bytes():
    pdf_url = url()
    return lib.Retriever.retrieve(pdf_url)


if __name__ == '__main__':
    app.run(port=8081, debug=True)
