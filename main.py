
#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import logging

from flask import Flask
import pypinyin
from pypinyin import pinyin, lazy_pinyin
import jieba
import thulac


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/cut/<text>')
def cut_text(text):
    return '::'.join(list(jieba.cut(text, cut_all=False)))

@app.route('/pinyin/<word>')
def show_pinyin(word):
    return ''.join(lazy_pinyin(word))
    # return word


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
