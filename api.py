from flask import Flask, request

from . import logic


app = Flask(__name__)


@app.route('/upload/', methods=['POST'])
def upload_data():
    file = request.files.get('file')
    logic.add_data(file)
    return '<p>Hello, World!</p>'


@app.route('/data/stats/<int:data_id>/')
def show_stats(data_id):
    stats = logic.get_stats(data_id)
    return '<p>Hello, World!</p>'


@app.route('/data/list/')
def show_list():
    return '<p>Hello, World!</p>'


@app.route('/data/clean/<int:data_id>/')
def clean_data(data_id):
    cleaned_data = logic.get_cleaned_data(data_id)
    return '<p>Hello, World!</p>'
