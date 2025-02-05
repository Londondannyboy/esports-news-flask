from flask import Flask, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_esports_news():
    headers = {
        'X-Api-Key': NEWS_API_KEY
    }
    
    params = {
        'q': 'esports OR "competitive gaming"',
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': 10
    }
    
    try:
        response = requests.get(NEWS_API_URL, headers=headers, params=params)
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
