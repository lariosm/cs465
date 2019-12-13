#!/usr/bin/env python
import requests
import json
import time


def _get_colors():
    get_url = "https://reqres.in/api/unknown"
    try:
        r = requests.get(get_url)
        if r.status_code == 200:
            colors = json.loads(r.text)
            print(colors["data"][0]["name"])
            print(colors["data"][1]["name"])
    except requests.exceptions.RequestException:
        print(f"Could not connect to the service at {get_url}")


def call_colors():

    while True:
        _get_colors()
        time.sleep(500)


if __name__ == "__main__":
    call_colors()
