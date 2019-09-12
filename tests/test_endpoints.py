import pytest
import requests
import os

url = 'http://127.0.0.1:5000' # The root url of the flask app


def test_index_page():
    r = requests.get(url+'/')
    assert r.status_code == 404


def test_base_api_page():
    r = requests.get(os.path.join(url, 'my_api', 'Contacts'))
    assert r.status_code == 200


def test_get_contacts():
    r = requests.get(os.path.join(url, 'my_api', 'Contacts'))
    data = r.json()
    assert len(data['data']) != 0

