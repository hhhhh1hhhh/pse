# 서버 생성
from fastapi import FastAPI
app = FastAPI()

# 실제 기능 추가
# 메인 페이지 접속 시 'hello' 보내기
#@app.get("/")
#def 작명():
#    return 'hello'

# 접속시 데이터 보내기
#@app.get("/data")
#def 작명():
#    return {'hello' : 1234}

# /docs 접속시 API 문서를 자동으로 만들어줌
# /redoc 다른 버전으로 API 문서를 만들어줌

# 메인페이지 접속시 html 파일 전송
from fastapi.responses import FileResponse
# DB 접속 코드 넣기

@app.get("/")
def 작명():
    # DB에서 데이터 꺼내는 코드 넣기
    return FileResponse('index.html')

# 유저한테 데이터를 받는 기능
# 유저가 이름, 연락처를 서버한테 보내고 싶은 경우 수신하는 기능(post)를 만들어주면 됨

# 유저한테 데이터를 받고 싶으면 모델부터 생성해야 함
from pydantic import BaseModel

# class에 유저들이 어떤 데이터를 보낼 수 있는지 명시, 타입과 함ㄱ
class Model(BaseModel):
    name :str
    phone :int    

@app.post("/send")
def 작명(data : Model):
    print(data)
    return '전송 완료'

# async/await 키워드로 비동기처리기능 가능
#@app.get("/")
#async def 작명():
    # await aabbscc (오른쪽에 있는 코드 aabbscc를 기다려줌)
    # DB에서 데이터 꺼내는 코드 넣기
#    return FileResponse('index.html')