from flask import Flask, jsonify
import time

app = Flask(__name__)


@app.route('/api/intdata/<int:id>', methods=["GET"])
def number(id):
    time.sleep(3)
    return jsonify({'even': (id % 2 == 0), 'inverted': -id})
