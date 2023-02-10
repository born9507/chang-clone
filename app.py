from flask import Flask, render_template, request
from bson import json_util
import json
from pymongo import MongoClient
client = MongoClient('mongodb 주소')
db = client.chang # db 이름 (chang)

app = Flask(__name__)

# / 주소로 GET 요청이 들어왔을 때, index.html 을 띄웁니다
@app.route('/')
def home():
    return render_template('index.html')

# /submit 주소로 POST 요청이 들어왔을 때, 아래 함수를 실행합니다
@app.route('/submit', methods=['POST'])
def submit_post():
    return json.loads(json_util.dumps())

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
