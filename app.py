from flask import Flask, jsonify, abort, request
from datetime import datetime


app = Flask(__name__)

activity_log = [
    {
        'id': 0,
        'user_id': 1,
        'username': 'john',
        'timestamp': datetime.utcnow(),
        'details': "Important stuff here",
    },
    {
        'id': 1,
        'user_id': 2,
        'username': 'yoko',
        'timestamp': datetime.utcnow(),
        'details': "Even more important",
    },
]


@app.route('/api/activities/', methods=["GET"])
def activities():
    return jsonify({'activities': activity_log})


@app.route('/api/activities/<int:id>', methods=["GET"])
def activity(id):
    if id < 0 or id >= len(activity_log):
        abort(404)
    return jsonify(activity_log[id])


@app.route('/api/activities', methods=["POST"])
def create_activity():
    if not request.json:
        abort(400)
    new_activity = request.get_json()
    if ('user_id' not in new_activity or 'username' not in new_activity or
            'details' not in new_activity):
        abort(400)
    new_activity['id'] = len(activity_log)
    new_activity['timestamp'] = datetime.utcnow()
    return jsonify(new_activity)
