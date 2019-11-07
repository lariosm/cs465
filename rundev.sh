#!/bin/bash
export WOLFIT_SETTINGS=$(pwd)/dev.settings
export URL=https://ml1-activitylog.herokuapp.com
flask run --host=0.0.0.0