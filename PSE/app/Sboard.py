# <게시판 만들기>
# 리스트 : find
# 작성 : insert
# 수정 : update
# 삭제 : delete

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from pymongo import MongoClient  # MongoDB연동#

# import datetime#
from datetime import datetime
from pytz import timezone


# 절대경로 지정#
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# MongoDB연동 https://wooiljeong.github.io/python/mongodb-01/ #
# HOST = "localhost"
# PORT = 27017  # 디폴트#
# client = MongoClient(HOST, PORT)  # client = MongoClient(f'mongodb://{HOST}:{PORT}')#
# db = client["PSE"]  # db접근#
# collection = db["CommunityBoard"]  # collection 접근#

mongodb_URL = "mongodb+srv://Jumin:wnwkao1356!@cluster0.hew1uqx.mongodb.net/test"
client = MongoClient(mongodb_URL)
db = client.PSE
collection = db.CommunityBoard


@app.get("/")
async def Sboard():
    return "python is so easy 커뮤니티 게시판"


# if GET인 경우 -> 그냥 페이지 보여주기#
@app.get(
    "/write", response_class=HTMLResponse
)  # response_class=HTMLResponse -> reponse타입을 html타입으로 해줌#
async def board_write(request: Request):
    print("get인 경우 실행")
    return templates.TemplateResponse(
        "./write.html", {"request": request}
    )  # templates.TemplateResponse() -> 어떤 데이터를 보낼지 명시하는 것#


# if post인 경우 -> 입력한 정보 가져오기#
@app.post("/write")
async def board_submit(name: str = Form(), title: str = Form(), contents: str = Form()):
    print("post인 경우 실행")
    # print(name, title, contents)

    # 내용 추가. add data#
    # collection = db["CommunityBoard"]  # collection 접근#

    # 작성시간 추가#
    # dt_kor = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    dt_kor = datetime.now(timezone("Asia/Seoul"))

    post = {
        "name": name,
        "title": title,
        "contents": contents,
        "date_kor": dt_kor,
    }  # 나중에 posting.py에 작성한 모델로 교체

    post_id = collection.insert_one(post).inserted_id
    print(post_id)

    return "성공적으로 게시됨"
    # return dt_kor#
