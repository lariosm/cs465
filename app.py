from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/api/intdata/<int:id>', methods=["GET"])
def number(id):
    num_data = [
        {
            'even': 'false',
            'inverted': '256'
        }
    ]

    return jsonify(num_data)
