#!/usr/bin/env bash
export FLASK_APP=app.py
export FLASK_ENV=development
export SLEEP_TIME=${2:-0}
set -a
. ./atlas.settings
set +a

flask run --host=localhost --port=$1