#!/bin/bash
export WOLFIT_SETTINGS=$(pwd)/dev.settings
export URL=http://localhost:8080
flask run --host=0.0.0.0