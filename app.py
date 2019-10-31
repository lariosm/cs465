from flask import Flask, jsonify


app = Flask(__name__)

# Creates and returns log entry
@app.route('/api/intdata/<int:id>', methods=["GET"])
def number(id):
    num_data = []
    if(id % 2 == 0):
        num_data['even'] = 1
    else:
        num_data['even'] = 2
    num_data['inverted'] = abs(id)
    return jsonify(num_data)
