from flask import Flask, render_template, send_from_directory
from app import app, logger
import requests as rq
from requests.compat import urljoin
import json
SCHEMA_REG_URL = '127.0.0.1:8081'

def endpoint(path):
    return urljoin("http://{0}".format(SCHEMA_REG_URL), path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assets/<path:path>')
def send_asset(path):
    return send_from_directory('assets', path)

@app.route('/subjects')
def schemas_index():
    subjects = rq.get(endpoint("/subjects")).json()
    logger.info(endpoint("/subjects"))
    logger.info(subjects)
    return render_template('subjects.html', subjects=subjects)

@app.route('/subjects/<string:subject>')
def subject_get(subject):
    subject = rq.get(endpoint("/subjects/{0}/versions/latest".format(subject))).json()
    return render_template('subject.html', subject=subject)