import string
import requests

possibilities = string.ascii_letters

url = 'https://bit.ly/4ti##p43'

for character in reversed(possibilities):
    new_url = url.replace('#', character, 1)
    for character in reversed(possibilities):
        new_new_url = new_url.replace('#', character)
        print(new_new_url)
        # response = None
        # try:
        #     response = requests.get(new_new_url)
        #     print(response.status_code)
        #     print(response.url)
        #     if response.status_code != 404:
        #         print("Valid URL")
        # except requests.exceptions.RequestException as e:  # This is the correct syntax
        #     print(e)
