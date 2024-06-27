#scrap webpage and get meaning information

import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract title and meta description
title = soup.title.string
meta_description = soup.find('meta', attrs={'name': 'description'})['content']

print(f'Title: {title}')
print(f'Meta Description: {meta_description}')
