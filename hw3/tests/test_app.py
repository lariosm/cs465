import sys
import requests
sys.path.append('..')


def test_return_all_activities():
    response = requests.get('http://0.0.0.0:5001/api/activities/')
    assert response.status_code == 200
