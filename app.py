from flask import Flask, jsonify, abort, request
from datetime import datetime
from mongoengine import connect, StringField, IntField, Document, \
    DateTimeField, queryset_manager
import json
from bson import ObjectId


app = Flask(__name__)
connect(db="act_log", host="localhost")


# MongoDB document that describes schema for log entries
class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow())
    details = StringField(required=True)

    @queryset_manager
    def objects(self, queryset):
        # By default, it orders queries by timestamp (most recent)
        return queryset.order_by('-timestamp')


# Returns all log entries
@app.route('/api/activities/', methods=["GET"])
def activities():
    logs = ActivityLog.objects[:10]  # Returns first 10 entries
    # Deserializes JSON document to python dict object
    json_logs = json.loads(logs.to_json())
    return jsonify({'activities': json_logs})


# Returns a single log entry
@app.route('/api/activities/<string:str_id>', methods=["GET"])
def activity(str_id):
    # Checks if input is valid (BSON) ObjectId object
    if ObjectId.is_valid(str_id):
        # Queries database by str_id and saves result to log_id
        log_id = ActivityLog.objects(id=str_id).first()
        if log_id is None:  # Does an entry with that str_id not exist?
            abort(404)
        # Deserializes JSON document to python dict object in readable format
        log_id_json = json.loads(log_id.to_json())
    return jsonify(log_id_json)


# Creates and returns log entry
@app.route('/api/activities/', methods=["POST"])
def create_activity():
    if not request.json:  # Is POST request in JSON format?
        abort(400)
    new_activity = request.get_json()  # Saves request to work with down below
    if ('user_id' not in new_activity or 'username' not in new_activity or
            'details' not in new_activity):
        abort(400)
    # Creates and saves log entry
    new_log = ActivityLog(
        user_id=new_activity['user_id'],
        username=new_activity['username'],
        details=new_activity['details']
    ).save()
    # Deserializes JSON document to python dict object in readable format
    new_log_json = json.loads(new_log.to_json())
    # Returns entry in JSON format with status code 201
    return jsonify(new_log_json), 201
