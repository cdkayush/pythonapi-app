import requests
import json
from random import randrange


def getData():
    random_number = str(randrange(10))
    x = requests.get('https://reqres.in/api/users/'+random_number)
    response = json.loads(x.text)
    print(response['data']['email'])   
    return x.text

getData()

