#importing all dependencies
import numpy as np
import requests
import base64

# Define your keys from the developer portal
consumer_key = 'A1KnlcOb0HyYRv1Y77plE6yFr'
consumer_secret = '0q1z0FFQlO6wnxbiIveo2JRZpsf5jIokFc6vXC4wCyUeHL5e0P'

# Reformat the keys and encode them
key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')

# Transform from bytes to bytes that can be printed
b64_encoded_key = base64.b64encode(key_secret)

# Transform from bytes back into Unicode
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
auth_data = {
    'grant_type': 'client_credentials'
}
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
print(auth_resp.status_code)
access_token = auth_resp.json()['access_token']

post_params = {
    'status': 'Hello World',
}
post_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
post_url = 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular'
post_resp = requests.post(post_url, headers=post_headers, params=post_params)

print(post_resp.json())