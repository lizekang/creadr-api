#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app

from flask import render_template, jsonify, request
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
    text = request.form.get('text').encode('utf-8')
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

