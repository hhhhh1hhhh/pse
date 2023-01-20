# <게시판 만들기>
# 리스트 : find
# 작성 : insert
# 수정 : update
# 삭제 : delete

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
<<<<<<< HEAD

# from fastapi.staticfiles import StaticFile
=======
>>>>>>> fca97f930c54a5d676bca907da0e2f94bf9af0b8
from fastapi.templating import Jinja2Templates
from pathlib import Path
from pymongo import MongoClient  # MongoDB연동#

<<<<<<< HEAD
# import datetime
=======
# import datetime#
>>>>>>> fca97f930c54a5d676bca907da0e2f94bf9af0b8
from datetime import datetime
from pytz import timezone

from bson.objectid import ObjectId


# 절대경로 지정#
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
<<<<<<< HEAD
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# MongoDB연동 https://wooiljeong.github.io/python/mongodb-01/ #
mongodb_URL = "mongodb+srv://"
=======
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# MongoDB연동 https://wooiljeong.github.io/python/mongodb-01/ #
mongodb_URL = "mongodb+srv://Jumin:wnwkao1356!@cluster0.hew1uqx.mongodb.net/test"
>>>>>>> fca97f930c54a5d676bca907da0e2f94bf9af0b8
client = MongoClient(mongodb_URL)
db = client.PSE  # db접근#
collection = db.CommunityBoard  # collection 접근#


@app.get("/")
async def community():
    return "python is so easy 커뮤니티 게시판"


<<<<<<< HEAD
@app.get("/view/{post_id}", response_class=HTMLResponse)  # 게시글 상세보기
async def Cboard_view(request: Request, post_id: str):
    idx = ObjectId(post_id)
    # 그 post_id(_id)에 해당하는 값 db에서 가져오기
    if idx is not None:
        data = collection.find_one({"_id": idx})
        if data is not None:  # data 존재o
            id = data.get("_id")
            name = data.get("name")
            title = data.get("title")
            contents = data.get("contents")
            date_kor = data.get("date_kor")
            return templates.TemplateResponse(
                "view.html",
                {
                    "request": request,
                    "id": id,
                    "name": name,
                    "title": title,
                    "contents": contents,
                    "date_kor": date_kor,
                },
            )
=======
@app.get("/view/{post_id}")  # 게시글 상세보기
async def Cboard_view(post_id=str, request=Request):
    idx = ObjectId(post_id)
    # 그 post_id(_id)에 해당하는 값 db에서 가져오기
    if idx is not None:
        data = collection.find_one({"_id": ObjectId(post_id)})
        if data is not None:  # data 존재o
            result = {
                "id": str(data.get("_id")),
                "name": data.get("name"),
                "title": data.get("title"),
                "contents": data.get("contents"),
                "date_kor": data.get("date_kor")
                # "view":data.get("view") #조회수
            }  # 이 data를 html로 전송해야함

            # return result["id"]
            return templates.TemplateResponse("./view.html", result=result)

    # return templates.TemplateResponse("./view.html", result)
    # return {"hello there, it's view"}
>>>>>>> fca97f930c54a5d676bca907da0e2f94bf9af0b8
    # return "not found"  # 404인 경우 추가해야함. flask의 abort와 같은 기능


# if GET인 경우 -> 그냥 페이지 보여주기#
@app.get(
    "/write", response_class=HTMLResponse
)  # response_class=HTMLResponse -> reponse타입을 html타입으로 해줌#
async def Cboard_write(request: Request):
    print("get인 경우 실행")
    return templates.TemplateResponse(
        "./write.html", {"request": request}
    )  # templates.TemplateResponse() -> 어떤 데이터를 보낼지 명시하는 것#


# if post인 경우 -> 입력한 정보 가져오기#
@app.post("/write")
async def Cboard_submit(
    name: str = Form(), title: str = Form(), contents: str = Form()
):
    print("post인 경우 실행")
    # 내용 추가. add data#

    # 작성시간 추가#
    # dt_kor = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    dt_kor = datetime.now(timezone("Asia/Seoul"))
    # time = round(datetime.utcnow().timestamp() * 1000)

    post = {
        "name": name,
        "title": title,
        "contents": contents,
        "date_kor": dt_kor,
        # "view": 0,  # 조회수. 디폴트 0#
    }  # 나중에 posting.py에 작성한 모델로 교체

    post_id = collection.insert_one(post).inserted_id
    return RedirectResponse(url="/view/" + str(post_id), status_code=303)
