#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app

from flask import render_template, jsonify, request, make_response
from pypinyin import pinyin, lazy_pinyin
import jieba
from creadr_text_processing import cut
import logging

@app.route('/')
def index():

    """Return index html."""

    return render_template('index.html')

@app.route('/api')
def all_api():
    # TODO:many things to do
    return jsonify({'api': ['various thing', 'so on', 'lol', '23333']})

@app.route('/api/getResult',methods=['POST'])
def return_json():
    '''response the post and return the result of cutting text
    post format {'text': '需要注意encode()0的是,'}
    Returns: jsonified data
    Examples:
        you should run server first (./manage.py runserver)
        >>> import requests
        >>> msg = {'text': '需要注意encode()0的是,'}
        >>> r = requests.post("http://127.0.0.1:8080/api/getResult", data=msg)
        >>> print(r.text)
    '''
    text = request.form.get('text').encode('utf-8')
    # resp = make_response(jsonify(cut(text)))
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    # resp.headers['Access-Control-Allow-Methods'] = 'POST'
    # resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    # return resp
    return jsonify(cut(text))

@app.route('/cut/<text>')
def cut_text(text):
    return '::'.join(list(jieba.cut(text, cut_all=False)))

@app.route('/pinyin/<word>')
def show_pinyin(word):
    return ''.join(lazy_pinyin(word))
    # return word

@app.errorhandler(404)
def server_error(e):
    # logging.exception('Not found error.')
    return render_template('errors/404.html', error=e), 404

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return render_template('errors/500.html', error=e), 500

