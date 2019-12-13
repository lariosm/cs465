from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime
from mongoengine import connect, StringField, IntField, Document, \
    DateTimeField, queryset_manager, ValidationError
import os
import time

app = Flask(__name__)

mongo_db = os.getenv('DB_NAME')
mongo_user = os.getenv('DB_USER')
mongo_password = os.getenv('DB_PASSWORD')
mongo_host = os.getenv('DB_HOST')
# Sets value for simulated latency
sleep_time = os.getenv('SLEEP_TIME', default=0)


# Connection settings to MongoDB cloud server
connect(host=mongo_host,
        db=mongo_db,
        username=mongo_user,
        password=mongo_password)


# MongoDB document that describes schema for log entries
class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow)
    details = StringField(required=True)

    @queryset_manager
    def objects(self, queryset):
        # By default, it orders queries by timestamp (most recent)
        return queryset.order_by('-timestamp')


def activity_helper(activity_object):
    # Turns document object to dictionary
    activity = activity_object.to_mongo().to_dict()
    activity["id"] = str(activity["_id"])  # Store Mongo-generated id to "id"
    activity.pop("_id")  # Remove to avoid raising TypeError exception
    activity["location"] = url_for("activity", str_id=activity["id"])

    return activity


# Returns all log entries
@app.route('/api/activities', methods=["GET"])
def activities():
    logs = ActivityLog.objects[:10]  # Returns first 10 entries
    log_list = [activity_helper(log) for log in logs]
    return jsonify({'activities': log_list})


# Returns a single log entry
@app.route('/api/activities/<string:str_id>', methods=["GET"])
def activity(str_id):
    try:
        # Queries database from string input and save it
        log_id = ActivityLog.objects(id=str_id)
        if log_id.first() is None:  # Does the log entry exist?
            abort(404)
        return jsonify(activity_helper(log_id.get()))
    except ValidationError:
        abort(400, f'\'{str_id}\' is not a valid ObjectId. It must be a'
              ' 12-byte input or a 24-character hex string.')

# Creates and returns log entry
@app.route('/api/activities', methods=["POST"])
def create_activity():
    if not request.json:  # Is POST request in JSON format?
        abort(400)
    new_activity = request.get_json()  # Saves request to work with down below
    # Checks if our JSON request contains the following keys to continue
    if ('user_id' not in new_activity or 'username' not in new_activity or
            'details' not in new_activity):
        abort(400)
    # Creates and saves log entry
    save_activity = ActivityLog(
        user_id=new_activity['user_id'],
        username=new_activity['username'],
        details=new_activity['details']
    ).save()
    time.sleep(int(sleep_time))  # Simulates latency in receiving a response
    # Queries database from created activity and saves it as Document object
    activity_obj = ActivityLog.objects(id=save_activity.id)
    return jsonify(activity_helper(activity_obj.get())), 201
