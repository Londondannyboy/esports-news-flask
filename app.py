from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

SERPER_API_KEY = os.getenv('SERPER_API_KEY')
SERPER_URL = "https://google.serper.dev/news"

def fetch_esports_news():
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    
    payload = {
        'q': 'esports news',
        'num': 10
    }
    
    try:
        response = requests.post(SERPER_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

@app.route('/api/news')
def get_news():
    news = fetch_esports_news()
    return jsonify(news)

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
