from flask import Flask, jsonify, request

from . import logic


app = Flask(__name__)


@app.route('/upload/', methods=['POST'])
def upload_data():
    """Функция для обработки POST запросов по добавлению данных."""
    if 'file' not in request.files:
        return 'File was not attached', 400
    file = request.files.get('file')
    if file.filename.split('.')[-1] != 'csv':
        return 'Wrong file format for uploading', 415
    try:
        logic.add_data(file)
    except Exception:
        return 'Server error', 500
    return jsonify({'response': 'data successfully uploaded'}), 201


@app.route('/data/stats/')
def show_stats():
    """Функция для обратоки GET запросов для получения статистики."""
    try:
        stats = logic.get_stats()
    except Exception:
        return 'Server error', 500
    return stats, 200


@app.route('/data/clean/')
def show_cleaned_data():
    """Функция для обработки GET запросов для получения очищенных данных."""
    try:
        cleaned_data = logic.get_cleaned_data()
    except Exception:
        return 'Server error', 500
    return cleaned_data, 200
