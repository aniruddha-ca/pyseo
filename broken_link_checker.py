import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a', href=True):
    link_url = link['href']
    try:
        link_response = requests.get(link_url)
        if link_response.status_code != 200:
            print(f'Broken link: {link_url}')
    except requests.exceptions.RequestException:
        print(f'Error with link: {link_url}')
