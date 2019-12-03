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
            print("Version: " + str(data[index - 1]["version"]))
            if data[index - 1]["version"] == 2.0:
                print("User IP: " + str(data[index - 1]["user_ip"]))
    except requests.exceptions.RequestException:
        print(f"Could not connect to the service at {get_url}")


if __name__ == "__main__":
    i = 0
    while i < 6:
        get_single_item(int(sys.argv[1]))
        time.sleep(3)
        i = i + 1
