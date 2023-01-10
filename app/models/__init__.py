'''
함수 안에 engine을 넣게 되면 다른 라우터에서는 사용할 수 없음
그러므로 __init__ 이라는 파일을 따로 만들어 엔진을 생성
'''
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from app.config import MONGO_DB_NAME, MONGO_URL


class MongoDB:
    def __init__(self):
        self.clientv = None
        self.engine = None
    
    def connect(self):  # DB 연결
        self.client = AsyncIOMotorClient(MONGO_URL)
        self.engine = AIOEngine(client=self.client, database=MONGO_DB_NAME)
        print("DB와 성공적으로 연결되었습니다.")
    
    def close(self):
        self.client.close()

mongodb = MongoDB()  # mongodb라는 인스턴스를 찍어줌. 싱글톤 패턴으로 단 한 번만 찍음
