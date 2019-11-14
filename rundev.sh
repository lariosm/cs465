#!/bin/bash
export WOLFIT_SETTINGS=$(pwd)/dev.settings
export URL=http://localhost:5001
flask run --host=localhost