import requests
import os
from dotenv import load_dotenv, find_dotenv

BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

load_dotenv(find_dotenv()) # This is to load your API keys from .env

params = {
    'q': 'gamestop',
    'api-key': os.getenv('NYT_KEY'),
}

response = requests.get(BASE_URL, params=params)
data = response.json()

for i in range(0, 10):
    print(data['response']['docs'][i]['headline']['main'])