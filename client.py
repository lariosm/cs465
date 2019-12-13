import requests
import json
import sys
import time


def get_single_item(index):
    get_url = "http://localhost:8080/api/posts"
    try:
        r = requests.get(get_url)
        if r.status_code == 200:
            data = json.loads(r.text)
            data_index = data[index - 1]
            print("Version: " + str(data_index["version"]))
            if data_index["version"] == 2.0:
                print("User IP: " + str(data_index["user_ip"]))
    except requests.exceptions.RequestException:
        print(f"Could not connect to the service at {get_url}")


if __name__ == "__main__":
    for i in range(10):
        time.sleep(5)
        # Retrieves single post data from a specified location via sys.argv
        # e.g. python client.py 2
        get_single_item(int(sys.argv[1]))
