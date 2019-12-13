import requests
import json
import sys


def get_single_item(index):
    get_url = "https://jsonplaceholder.typicode.com/todos/"
    try:
        r = requests.get(get_url)
        if r.status_code == 200:
            data = json.loads(r.text)
            print(data[index - 1])
    except requests.exceptions.RequestException:
        print(f"Could not connect to the service at {get_url}")


if __name__ == "__main__":
    get_single_item(int(sys.argv[1]))
