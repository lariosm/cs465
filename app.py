from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/api/intdata/<int:id>', methods=["GET"])
def number(id):
    if(id % 2 == 0):
        return jsonify({'even': 'true', 'inverted': -id})
    return jsonify({'even': 'false', 'inverted': -id})
