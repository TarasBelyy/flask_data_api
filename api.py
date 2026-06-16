from flask import Flask, request

from . import logic


app = Flask(__name__)


@app.route('/upload/', methods=['POST'])
def upload_data():
    file = request.files.get('file')
    logic.add_data(file)
    return '<p>Succesfully added new data</p>'


@app.route('/data/stats/')
def show_stats():
    stats = logic.get_stats()
    return stats


@app.route('/data/clean/')
def show_cleaned_data():
    cleaned_data = logic.get_cleaned_data()
    return '<p>Hello, World!</p>'
