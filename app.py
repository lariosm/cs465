from flask import Flask, jsonify, abort, request
from datetime import datetime
from mongoengine import connect, StringField, IntField, Document, DateTimeField
import json


app = Flask(__name__)
connect(db="act_log", host="localhost")


class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow())
    details = StringField(required=True)


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
    logs = ActivityLog.objects[:10]
    return jsonify({'activities': json.loads(logs.to_json())})
    # return jsonify({'activities': activity_log})


@app.route('/api/activities/<id>', methods=["GET"])
def activity(id):
    # if id < 0 or id >= len(activity_log):
    #    abort(404)
    return jsonify(json.loads(ActivityLog.objects(_id=id).first().to_json()))


@app.route('/api/activities/', methods=["POST"])
def create_activity():
    if not request.json:
        abort(400)
    new_activity = request.get_json()
    if ('user_id' not in new_activity or 'username' not in new_activity or
            'details' not in new_activity):
        abort(400)
    new_log = ActivityLog(
        user_id=new_activity['user_id'],
        username=new_activity['username'],
        details=new_activity['details']
    ).save()
    # new_activity['id'] = len(activity_log)
    return jsonify(json.loads(new_log.to_json())), 201
