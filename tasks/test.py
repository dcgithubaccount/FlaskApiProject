import celery
import requests
import os
import random

url = 'http://127.0.0.1:5000'
end_point = os.path.join(url, 'my_api', 'Contacts')


@celery.task()
def post_periodic_contacts():
    random_num = random.randint(1, 100)
    username = 'user' + str(random_num)
    first_name = username + 'Cho'
    last_name = 'Smith' if random_num%2 == 0 else 'Mrs Smith'
    email = first_name+'.'+last_name+'@.example.com'
    inp = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }
    r = requests.post(url=end_point, json=inp)






