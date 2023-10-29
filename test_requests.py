import requests
import json

session = requests.Session()

API = 'http://localhost/api'


# python3 -m pytest -rP -k test_post_consumptions
def test_post_consumptions():
    headers = {
        'Content-Type': 'application/json'
    }
    data = {'wow': 'great'}

    r = session.post(
        f'{API}/consumptions/junhg0211',
        headers=headers, data=json.dumps(data))

    print(r.text)
