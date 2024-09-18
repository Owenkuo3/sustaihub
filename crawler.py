import requests
from bs4 import BeautifulSoup
import sqlite3
import schedule
import time

def create_connection():
    conn = sqlite3.connect('news.db')
    return conn

def create_table():
    conn = create_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL
            )
        ''')

def fetch_news():
    try:
        url = "https://www.bbc.com/news/science_and_environment"
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        span_elements = soup.find_all('span', {'aria-hidden': 'false'})
        
        conn = create_connection()
        with conn:
            for span in span_elements:
                title = span.get_text()
                if len(title.split()) >= 2:
                    conn.execute('INSERT INTO news (title) VALUES (?)', (title,))
    
        print("News fetched and stored.")
    except Exception as e:
        print(f"An error occurred: {e}")


def job():
    fetch_news()

create_table()

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
