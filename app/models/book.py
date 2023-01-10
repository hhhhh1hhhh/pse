"""
실제 사용할 모델: book
하나의 데이터, 하나의 document라고 생각하면 됨
"""

from odmantic import AIOEngine, Model


class BookModel(Model):  # BookModel: 이 프로젝트에서는 책을 수집하는데, 책에서 어떤 데이터를 수집할지 적어놓음
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"


# MongoDB(fastapi-pj)는 Data 안에 Collection(books)이 있음. Collection 안에는 document가 있음
# document 안에는
"""
    keyword: str
    publisher: str
    price: int
    image: str
"""
# 이런 식으로 정보가 담김
