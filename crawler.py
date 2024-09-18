import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news/science_and_environment"
response = requests.get(url)

response.encoding = 'utf-8'

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
        
    span_elements = soup.find_all('span', {'aria-hidden': 'false'})

    for span in span_elements:
        title = span.get_text().strip()
        
        if len(title.split()) >= 2:
            print(title)

else:
    print("Failed to retrieve the webpage")