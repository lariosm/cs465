from flask import Flask, json, url_for
import sys
sys.path.append('..')
import pytest
import requests
import app


def test_return_all_activities():
    response = requests.get('http://0.0.0.0:5001/api/activities/')
    assert response.status_code == 200
