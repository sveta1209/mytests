import json
from urllib import request, response
import pytest
import requests

def test_create_post():

    url = 'http://localhost:5000/posts'
    payload = { "title": "Study",
                "text": "Go ahead",
                "author_id": 1}

    response = requests.post(url, json=payload)
    status_code = response.status_code
    assert status_code == 201








