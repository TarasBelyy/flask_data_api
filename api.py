from flask import Flask, jsonify, request

from . import logic


app = Flask(__name__)


@app.route('/upload/', methods=['POST'])
def upload_data():
    """Функция для обработки POST запросов по добавлению данных."""
    file = request.files.get('file')
    logic.add_data(file)
    return jsonify({'response': 'data successfully uploaded'}), 201


@app.route('/data/stats/')
def show_stats():
    """Функция для обратоки GET запросов для получения статистики."""
    stats = logic.get_stats()
    return stats, 200


@app.route('/data/clean/')
def show_cleaned_data():
    """Функция для обработки GET запросов для получения очищенных данных"""
    cleaned_data = logic.get_cleaned_data()
    return cleaned_data, 200
