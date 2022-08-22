import pytest
import requests
import os

url = 'http://127.0.0.1:5000'
end_point = os.path.join(url, 'my_api', 'Contacts')


def test_index_page():
    r = requests.get(f'{url}/')
    assert r.status_code == 404


def test_base_api_page():
    r = requests.get(url=end_point)
    assert r.status_code == 200


def test_get_contacts():
    r = requests.get(url=end_point)
    data = r.json()
    assert len(data['data']) != 0


def test_post_contacts():
    inp = {
        'username': 'user3',
        'first_name': 'MedCho',
        'last_name': 'Isabella',
        'email': 'isabella@email.com'
    }
    r = requests.post(url=end_point, json=inp)
    assert r.status_code == 201


def test_put_contacts():
    inp = {
        "username": "user2"
    }
    r = requests.get(end_point, json=inp)
    data = r.json()['data']
    mod_input = {
        'id': data['id'],
        'email_two': 'second_one@email.com',
        'email_three': 'third_one@example.com'
    }
    mod = requests.put(url=end_point, json=mod_input)
    assert mod.status_code == 204


def test_delete_contacts():
    inp = {
        "username": "user3"
    }
    r = requests.get(end_point, json=inp)
    data = r.json()['data']
    mod_input = {
        'id': data['id']
    }
    mod = requests.delete(url=end_point, json=mod_input)
    assert mod.status_code == 204
