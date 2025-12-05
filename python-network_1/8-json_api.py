#!/usr/bin/python3
"""Search API that sends a POST request with a letter and handles JSON response.
If no argument is given, sets q to an empty string.
"""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}

    try:
        response = requests.post(url, data=payload)
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
