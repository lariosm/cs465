from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime

appl = Flask(__name__)


VOTES = [
    {
        'post_id': 0,
        'vote_count': -1,
    },
    {
        'post_id': 1,
        'vote_count': 5,
    },
    {
        'post_id': 2,
        'vote_count': 42,
    },
]


# Returns all log entries
@appl.route('/api/votes', methods=["GET"])
def votes():
    return jsonify(VOTES)


# Returns a single log entry
@appl.route('/api/votes/<int:post_id>', methods=["GET"])
def vote(post_id):
    return jsonify(VOTES[post_id])