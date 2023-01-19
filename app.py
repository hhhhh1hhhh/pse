"""
1. html파일과 연결해보기
연결하기 전 프로젝트 파일에 templates와 static 폴더를 만들어
templates에는 html파일을, static에는 css파일이나 이미지 파일이 들어간다.
포트번호 5000으로 index html과 연결한다.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=6000, debug=True)
"""

"""
2. API 만들기
GET, POST 방식을 이용하여 데이터를 주고 받는 것을 연습한다.
GET은 데이터를 조회하고, POST는 데이터 생성, 변경, 삭제이다.


from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test', methods=['GET'])
def test_get():
    title = request.args.get('title')
    return jsonify({'msg': '이 요청은 GET!', 'title' : title})


@app.route('/test', methods=['POST'])
def test_post():
    fruit_name = request.form['fruit_name']
    doc = {'fruit_name': fruit_name}
    db.fruit.insert_one(doc)
    return jsonify({'msg': '저장 완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
"""

"""3. MongoDB에 데이터 저장하기"""

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
client = MongoClient('mongodb+srv://jaeyeon:<qwe123>@cluster0.zrmacy9.mongodb.net/?retryWrites=true&w=majority')

db = client.hobby

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/test', methods=['GET'])
def test_get():
    fruit_list = list(db.fruit.find({}, {'_id': False}))
    return jsonify({'fruits': fruit_list})


@app.route('/test', methods=['POST'])
def test_post():
    fruit_name = request.form['fruit_name']
    doc = {'fruit_name': fruit_name}
    db.fruit.insert_one(doc)
    return jsonify({'msg': '저장 완료'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
